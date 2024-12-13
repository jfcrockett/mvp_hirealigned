import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional, Union
import streamlit as st
from pyairtable import Api
import os
from dotenv import load_dotenv

@dataclass
class CultureBaseline:
   purpose = {
       "values": "Patient-centered care, making smiles about more than teeth",
       "passion": "Pride in providing exceptional care and education",
       "vision": "Creating lasting positive impact on patients' lives"
   }
   people = {
       "vibe": "Supportive, collaborative, family-like atmosphere", 
       "team": "Strong emphasis on teamwork and mutual support",
       "association": "Deep connection to colleagues and workplace"
   }
   priorities = {
       "time": "Work-life balance, efficient patient care",
       "impact": "Patient satisfaction and health outcomes", 
       "growth": "Professional development and continuous improvement"
   }

@dataclass
class CandidateScore:
   name: str
   email: Optional[str]
   scores: Dict[str, Union[int, str]]
   highlights: Dict[str, str]
   suborganization: str
   role: str

class CultureFitAnalysis:
   def __init__(self):
       load_dotenv()
       self.baseline = CultureBaseline()
       self.organization = st.query_params.get("org", "Liberty Dental")
       self.candidates = self._init_candidates()

   def _get_airtable_data(self, table_name):
       """Get data from Airtable table."""
       api = Api(os.getenv('AIRTABLE_API_KEY'))
       base_id = os.getenv('BASE_ID')
       table = api.table(base_id, table_name)
       records = table.all()
       
       # Create DataFrame with fields
       if records:
           df = pd.DataFrame([record['fields'] for record in records])
           return df
       return pd.DataFrame()

   def _init_candidates(self) -> List[CandidateScore]:
       """Initialize candidates from Airtable data."""
       scores_df = self._get_airtable_data("Candidate Scores")
       responses_df = self._get_airtable_data("Candidate Responses")
       
       # Filter responses by organization first
       responses_df = responses_df[responses_df['Organization'] == self.organization]
       
       # Get unique combinations of suborganization and role
       self.filter_options = sorted(
           list(set([
               f"{row['Sub-Organization']} - {row['hidden_role']}" 
               for _, row in responses_df.iterrows() 
               if pd.notna(row['Sub-Organization']) and pd.notna(row['hidden_role'])
           ]))
       )
       
       # Convert 'created' to datetime and sort by it
       if 'created' in scores_df.columns:
           scores_df['created'] = pd.to_datetime(scores_df['created'])
           scores_df = scores_df.sort_values('created', ascending=False)
           scores_df = scores_df.drop_duplicates(subset=['Name'], keep='first')
       
       candidates = []
       
       # First, create a mapping of response_id to organization info
       response_info = {}
       for _, response in responses_df.iterrows():
           response_info[response['id']] = {
               'suborganization': response.get('Sub-Organization', ''),
               'role': response.get('hidden_role', ''),
               'email': response.get('email', None)
           }
       
       for _, score_row in scores_df.iterrows():
           try:
               response_id = score_row.get('response_id')
               
               # Skip if no response_id or if response not in filtered organization
               if not response_id or response_id not in response_info:
                   continue
               
               # Get organization info from our mapping
               org_info = response_info[response_id]
               
               scores = {
                   "purpose": score_row.get('purpose score'),
                   "people": score_row.get('people score'),
                   "priorities": score_row.get('priority score')
               }
               
               # Convert scores to integers if they're strings
               scores = {k: int(v) if isinstance(v, str) and v.isdigit() else v 
                        for k, v in scores.items()}
               
               candidate = CandidateScore(
                   name=score_row.get('Name', 'Unknown'),
                   email=org_info['email'],
                   scores=scores,
                   highlights={
                       "purpose": score_row.get('purpose description', 'No description available'),
                       "people": score_row.get('people description', 'No description available'),
                       "priorities": score_row.get('priority description', 'No description available')
                   },
                   suborganization=org_info['suborganization'],
                   role=org_info['role']
               )
               
               candidates.append(candidate)
               print(f"Successfully processed candidate: {candidate.name} - {candidate.suborganization} - {candidate.role}")
               
           except Exception as e:
               st.error(f"Error processing candidate: {score_row.get('Name', 'Unknown')} - {str(e)}")
               print(f"Error details for {score_row.get('Name', 'Unknown')}:")
               print(f"Score row data: {score_row.to_dict()}")
               continue
       
       return candidates

   def get_score_color(self, score: Union[int, str]) -> str:
       if score is None or score == "NA":
           return "#D3D3D3"  # light gray
       if score >= 8:
           return "#90EE90"  # light green
       if score >= 6:
           return "#FFD700"  # light gold
       return "#FFB6C1"      # light pink

   def get_average_score(self, scores: Dict[str, Union[int, str]]) -> Union[float, str]:
       """Calculate average score, handling NA values."""
       valid_scores = [score for score in scores.values() if isinstance(score, (int, float))]
       if not valid_scores:
           return "NA"
       return round(sum(valid_scores) / len(valid_scores), 1)

   def sort_candidates(self):
       """Sort candidates by average score, highest first."""
       self.candidates.sort(
           key=lambda x: (
               -1 if isinstance(self.get_average_score(x.scores), str) 
               else self.get_average_score(x.scores)
           ),
           reverse=True
       )

   def display_dashboard(self):
       # Create sidebar for filter
       with st.sidebar:
           st.title("Filters")
           
           # Combined filter for suborganization and role
           selected_filter = st.selectbox(
               "Select Team and Role",
               options=["All"] + self.filter_options
           )

       # Create two columns for the logo and title
       logo_col, title_col = st.columns([1, 5])

       with logo_col:
           try:
               st.image("./HireBlack.jpg", width=150)
           except:
               st.write("HireAligned")

       with title_col:
           st.title(f"HireAligned - {self.organization}")

       # Display baseline
       st.header(f"{self.organization}: Organizational Baseline")
       cols = st.columns(3)
       with cols[0]:
           st.subheader("Purpose")
           st.write(self.baseline.purpose["values"])
       with cols[1]:
           st.subheader("People")
           st.write(self.baseline.people["vibe"])
       with cols[2]:
           st.subheader("Priorities")
           st.write(self.baseline.priorities["time"])

       # Filter candidates based on selection
       filtered_candidates = self.candidates
       if selected_filter != "All":
           suborg, role = selected_filter.split(" - ")
           filtered_candidates = [
               c for c in filtered_candidates 
               if c.suborganization == suborg and c.role == role
           ]

       # Sort filtered candidates by average score
       filtered_candidates.sort(
           key=lambda x: (
               -1 if isinstance(self.get_average_score(x.scores), str) 
               else self.get_average_score(x.scores)
           ),
           reverse=True
       )

       # Display candidates
       st.header(f"Candidate Assessments: {selected_filter}")
       
       for i, candidate in enumerate(filtered_candidates):
           if i > 0:
               st.markdown('<hr style="border: 2px solid #ddd;">', unsafe_allow_html=True)
            
           cols = st.columns([3, 1])
           with cols[0]:
               st.subheader(candidate.name)
               if candidate.email:
                   st.write(candidate.email)
           with cols[1]:
               avg = self.get_average_score(candidate.scores)
               st.metric("Average Score", avg)

           score_cols = st.columns(3)
           for i, category in enumerate(["purpose", "people", "priorities"]):
               with score_cols[i]:
                   score = candidate.scores[category]
                   color = self.get_score_color(score)
                   st.markdown(f"_{category.title()}_")
                   st.markdown(
                       f'<div style="background-color: {color}; padding: 5px; border-radius: 5px; text-align: center; color: black;">'
                       f'<strong>{score}</strong></div>',
                       unsafe_allow_html=True
                   )
                   st.markdown(f"_{candidate.highlights[category]}_")

if __name__ == "__main__":
   dashboard = CultureFitAnalysis()
   dashboard.display_dashboard()
