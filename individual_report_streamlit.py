# cultural_alignment_streamlit.py

import streamlit as st
import os
from pyairtable import Api
from dotenv import load_dotenv
import pandas as pd

def load_candidate_data():
    """Load all candidates from Airtable Candidate Scores table."""
    api = Api(os.getenv('AIRTABLE_API_KEY'))
    base_id = os.getenv('BASE_ID')
    scores_table = api.table(base_id, "Candidate Scores")
    records = scores_table.all()
    
    # Convert to DataFrame for easier handling
    if records:
        df = pd.DataFrame([record['fields'] for record in records])
        return df
    return pd.DataFrame()

def display_score_gauge(score, title):
    """Display a score using Streamlit progress bar."""
    st.subheader(title)
    score_as_percentage = float(score) / 10.0  # Convert 0-10 score to 0-1.0 range
    st.progress(score_as_percentage)
    st.write(f"Score: {score}/10")

def display_candidate_report(candidate_data):
    """Display the cultural alignment report for a single candidate."""
    # Logo and Title in columns
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("assets/hireblack.jpg", width=150)  # Adjust path and width as needed
    with col2:
        st.title("HireAligned Candidate Alignment Report")
    
    # Introduction about HireAligned
    st.markdown("""
    ### About This Report
    
    At HireAligned, we believe that culture and value alignment matters, and not just for the hiring company. We are commited to empowering companies to build
                a place where people are aligned with the company's values and culture and can thrive. 
    Unlike traditional assessments that only serve employers, we share these insights directly with you because we 
    believe in helping job candidates also make informed decisions when they are deciding what company to join.
    
    This report comes from the conversational survey you took recently when you applied to a job. Use these insights to evaluate potential opportunities. 
                
    If you have any questions or feedback, please reach out to <a href="mailto:team@hirealigned.com">team@hirealigned.com</a>.
    """, unsafe_allow_html=True)
    
    st.markdown("---")  # Divider line
    
    # Header Information
    st.header("Candidate Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Name:** {candidate_data['Name']}")
    with col2:
        st.write(f"**Response ID:** {candidate_data['response_id']}")
    
    st.markdown("---")  # Divider line
    
    # Candidate Summary
    st.header("Candidate Summary")
    st.write(candidate_data['executive summary'])
    
    st.markdown("---")  # Divider line
    
    # Role Specific Alignment Scores
    st.header("Role Specific Alignment Scores")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        display_score_gauge(candidate_data['fit score'], "Fit")
        st.write("**Fit Analysis:**")
        st.write(candidate_data['fit description'])
    
    with col2:
        display_score_gauge(candidate_data['fulfillment score'], "Fulfillment")
        st.write("**Fulfillment Analysis:**")
        st.write(candidate_data['fulfillment description'])
    
    with col3:
        display_score_gauge(candidate_data['future score'], "Future")
        st.write("**Future Analysis:**")
        st.write(candidate_data['future description'])
    
    st.markdown("---")  # Divider line
    
    # General Career Feedback
    st.header("General Career Feedback")
    
    # Key Strengths
    st.subheader("Key Strengths")
    strengths = candidate_data['key_strengths'].split('\n') if isinstance(candidate_data['key_strengths'], str) else []
    for strength in strengths:
        if strength.strip():
            st.markdown(f"• {strength.strip()}")
    
    # Development Areas
    st.subheader("Development Areas")
    areas = candidate_data['development_areas'].split('\n') if isinstance(candidate_data['development_areas'], str) else []
    for area in areas:
        if area.strip():
            st.markdown(f"• {area.strip()}")
    
    st.markdown("---")  # Divider line
    
    # Next Employer Fit
    st.header("Things to Look for in Next Employer")
    st.write(candidate_data['things_to_look_for'])
    
    # Footer with HireAligned link
    st.markdown("---")  # Final divider line
    st.markdown(
        "<div style='text-align: center;'>"
        "<p>Powered by <a href='https://www.hirealigned.com' target='_blank'>HireAligned</a></p>"
        "</div>", 
        unsafe_allow_html=True
    )

def main():
    """Main Streamlit app."""
    st.set_page_config(
        page_title="Cultural Alignment Reports",
        page_icon="🎯",
        layout="wide"
    )
    
    # Load environment variables
    load_dotenv()
    
    # Load candidate data
    candidates_df = load_candidate_data()
    
    if candidates_df.empty:
        st.error("No candidate data found in Airtable.")
        return
    
    # Get candidate ID from URL, default to specified ID if none provided
    candidate_id = st.query_params.get('id', "3521541545511618729")
    
    candidate_data = candidates_df[candidates_df['response_id'] == candidate_id]
    if not candidate_data.empty:
        display_candidate_report(candidate_data.iloc[0])
    else:
        st.markdown(
            "🤔 It looks like the candidate you are looking for either doesn't exist, "
            "or they didn't complete enough info in their candidate assessment. "
            "Please reach out to <a href='mailto:team@hirealigned.com'>team@hirealigned.com</a> for help.",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()