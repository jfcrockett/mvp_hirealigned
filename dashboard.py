import pandas as pd
from dataclasses import dataclass
from typing import Dict, List, Optional, Union
import streamlit as st

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

class CultureFitAnalysis:
   def __init__(self):
       self.baseline = CultureBaseline()
       self.candidates = self._init_candidates()

   def _init_candidates(self) -> List[CandidateScore]:
       return [
           CandidateScore(
               name="Ariele Retherford",
               email="ariele.retherford@outlook.com",
               scores={"purpose": 8, "people": 9, "priorities": 9},
               highlights={
                   "purpose": "Passionate about coordinating and building career impact",
                   "people": "Strong team collaboration and communication skills", 
                   "priorities": "Proactive in personal development and time management"
               }
           ),

           CandidateScore(
               name="Rajae Penrod",
               email="rajaestock@yahoo.com",
               scores={"purpose": 9, "people": 8, "priorities": 8},
               highlights={
                   "purpose": "12 years dental experience with focus on patient care",
                   "people": "Values team achievement and collaborative success",
                   "priorities": "Strong work-life balance and emergency response"
               }
           ),

           CandidateScore(
               name="Kimberlee Talbot", 
               email="kimberleetalbot18@gmail.com",
               scores={"purpose": 8, "people": 8, "priorities": 8},
               highlights={
                   "purpose": "Genuine interest in dentistry since high school",
                   "people": "Shows empathy and understanding with colleagues",
                   "priorities": "Balanced approach to urgent tasks and family time"
               }
           ),

           CandidateScore(
               name="Brianna Cuevas",
               email="briannacuevastate@gmail.com", 
               scores={"purpose": 8, "people": 8, "priorities": 8},
               highlights={
                   "purpose": "Focus on creating positive impact and helping others",
                   "people": "Strong communication and team management skills",
                   "priorities": "Demonstrates consideration and work-life balance"
               }
           ),

           CandidateScore(
               name="Liberty Burghardt",
               email="bewentzecl@gmail.com",
               scores={"purpose": 7, "people": 9, "priorities": 8},
               highlights={
                   "purpose": "Creative problem-solver with customer focus",
                   "people": "Excellence in collaborative environments",
                   "priorities": "Strong organizational and planning skills"
               }
           ),

           CandidateScore(
               name="Nyla Rattanakone",
               email="nylarattanakone@gmail.com",
               scores={"purpose": 7, "people": 8, "priorities": 8},
               highlights={
                   "purpose": "Customer service focused with pride in service quality",
                   "people": "Experience managing high-pressure team situations",
                   "priorities": "Strong work ethic and adaptability"
               }
           ),

           CandidateScore(
               name="Yamileth Moreno",
               email="yamilethvargas2003@gmail.com",
               scores={"purpose": 7, "people": 8, "priorities": 8},
               highlights={
                   "purpose": "Strong customer service and communication skills",
                   "people": "Thrives in team environments during high-stress periods",
                   "priorities": "Shows initiative and responsibility"
               }
           ),

           CandidateScore(
               name="Andrea Escobar",
               email="andrea79609@gmail.com",
               scores={"purpose": 8, "people": 7, "priorities": 8},
               highlights={
                   "purpose": "Passionate about helping patients feel confident",
                   "people": "Strong communication and problem-solving skills",
                   "priorities": "Shows adaptability and initiative"
               }
           ),

           CandidateScore(
               name="Savanna Pratt",
               email="Aviepratt8@gmail.com",
               scores={"purpose": 7, "people": 8, "priorities": 7},
               highlights={
                   "purpose": "Focus on developing communication skills",
                   "people": "Values supportive team environment",
                   "priorities": "Shows initiative in time management"
               }
           ),

           CandidateScore(
               name="Chelsea Antonson",
               email="chelsea.antonson@gmail.com",
               scores={"purpose": 7, "people": 8, "priorities": 7},
               highlights={
                   "purpose": "Passion for teaching and learning from others",
                   "people": "Creates positive work environments",
                   "priorities": "Strong work ethic and dedication"
               }
           ),

           CandidateScore(
               name="Cheri Moody",
               email="cheri4443@gmail.com",
               scores={"purpose": 8, "people": 7, "priorities": 7},
               highlights={
                   "purpose": "Strong interest in medical field and helping others",
                   "people": "Values teamwork and direct communication",
                   "priorities": "Demonstrates commitment to deadlines"
               }
           ),

           CandidateScore(
               name="Jalizah Kelley",
               email="Kelleyjalizah@gmail.com",
               scores={"purpose": 7, "people": 7, "priorities": 8},
               highlights={
                   "purpose": "Seeking growth opportunities and new experiences",
                   "people": "Professional approach to team dynamics",
                   "priorities": "Strong initiative in skill development"
               }
           ),

           CandidateScore(
               name="Israel Andaverde",
               email="Andaverdeisrael@gmail.com",
               scores={"purpose": 7, "people": 7, "priorities": 7},
               highlights={
                   "purpose": "Shows initiative and attention to detail",
                   "people": "Values authentic team relationships",
                   "priorities": "Demonstrates proactive work ethic"
               }
           ),

           CandidateScore(
               name="Kamaria James",
               email="kamariamichelle10@gmail.com",
               scores={"purpose": 7, "people": 7, "priorities": 7},
               highlights={
                   "purpose": "Family influence in dental field",
                   "people": "Experience in conflict resolution",
                   "priorities": "Shows dedication to responsibilities"
               }
           ),

           CandidateScore(
               name="Tiffany Lupton",
               email="Luptontiffany1011@gmail.com",
               scores={"purpose": 8, "people": 7, "priorities": 7},
               highlights={
                   "purpose": "19 years dental assisting experience",
                   "people": "Values cross-training and team learning",
                   "priorities": "Seeks professional growth opportunities"
               }
           ),

           CandidateScore(
               name="Adrianna Camacho",
               email="adriannacamacho13@gmail.com",
               scores={"purpose": 7, "people": 7, "priorities": 7},
               highlights={
                   "purpose": "Committed to specialized patient experience",
                   "people": "Inspired by compassionate team environments",
                   "priorities": "Motivated to contribute to team success"
               }
           ),

           CandidateScore(
               name="Isela Lopez",
               email="lopezisela123@icloud.com",
               scores={"purpose": None, "people": None, "priorities": None},
               highlights={
                   "purpose": "Insufficient information provided",
                   "people": "Unable to assess team compatibility",
                   "priorities": "Need more details on work style"
               }
           ),

           CandidateScore(
               name="Hailey Raya",
               email="haileyyazmin@gmail.com",
               scores={"purpose": None, "people": None, "priorities": None},
               highlights={
                   "purpose": "Insufficient information provided",
                   "people": "Limited data on team interaction style",
                   "priorities": "Need more details on work priorities"
               }
           ),

           CandidateScore(
               name="Anniss",
               email=None,
               scores={"purpose": None, "people": None, "priorities": None},
               highlights={
                   "purpose": "No detailed information provided",
                   "people": "Unable to assess team compatibility",
                   "priorities": "Insufficient data on work approach"
               }
           ),

           CandidateScore(
               name="Jeff Galica",
               email="Jgalica27@gmail.com",
               scores={"purpose": None, "people": None, "priorities": None},
               highlights={
                   "purpose": "Limited information available",
                   "people": "Insufficient data on team interaction",
                   "priorities": "Need more details on work style"
               }
           ),

           CandidateScore(
               name="Tanya",
               email=None,
               scores={"purpose": None, "people": None, "priorities": None},
               highlights={
                   "purpose": "No detailed information provided",
                   "people": "Unable to assess team fit",
                   "priorities": "Insufficient data for evaluation"
               }
           )
       ]

   def get_score_color(self, score: Union[int, str]) -> str:
       if score is None or score == "NA":
           return "#D3D3D3"  # light gray
       if score >= 8:
           return "#90EE90"  # light green
       if score >= 6:
           return "#FFD700"  # light gold
       return "#FFB6C1"      # light pink

   def get_average_score(self, scores: Dict[str, Union[int, str]]) -> Union[float, str]:
       valid_scores = [score for score in scores.values() if isinstance(score, int)]
       if not valid_scores:
           return "NA"
       return round(sum(valid_scores) / len(valid_scores), 1)

   def sort_candidates(self):
       self.candidates.sort(
           key=lambda x: (
               -1 if isinstance(self.get_average_score(x.scores), str) 
               else self.get_average_score(x.scores)
           ),
           reverse=True
       )

   def display_dashboard(self):
       # Create two columns for the logo and title
       logo_col, title_col = st.columns([1, 5])  # Adjust the ratio as needed

       with logo_col:
           st.image("./HireBlack.jpg", width=150)  # Adjust the path and width as needed

       with title_col:
           st.title("HireAligned")

       # Display baseline
       st.header("Liberty Dental: Organizational Baseline")
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

       # Display candidates
       st.header("Candidate Assessments: Scheduling Coordinator")
       self.sort_candidates()
       
       for i, candidate in enumerate(self.candidates):
           if i > 0:  # Add a divider before each candidate (except the first one)
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
