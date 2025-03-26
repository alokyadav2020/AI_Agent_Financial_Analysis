from crewai import Agent,LLM
from tools import search_tool

from dotenv import load_dotenv
import streamlit as st
load_dotenv()
import os


from langchain_huggingface import HuggingFaceEndpoint
st.secrets("HUGGINGFACE_API_KEY")
st.secrets("SERPER_API_KEY")

os.environ["HUGGINGFACE_API_KEY"] = os.getenv(st.secrets("SERPER_API_KEY"))
llm =HuggingFaceEndpoint(repo_id="huggingface/meta-llama/Llama-3.3-70B-Instruct",max_new_tokens=6000)


# Define the agents

blog_researcher=Agent(
    role='Market Researcher from internet',
    goal="get the relevant market report for the industry {topic} from the provided internet data",
    llm=llm,
          
    verboe=False,
    memory=True,
    backstory=(
       "Expert in understanding financial market reports in relevent industry and providing suggestion" 
       "You collect following information"
       "**Industry Overview:** Current state and future outlook of the industry. (IBIS)"
       "**Market Share Analysis:** Pie charts illustrating the company's share relative to competitors."
       "**SWOT Analysis:** Matrix highlighting strengths, weaknesses, opportunities, and threats."
       "**Customer Analysis: Breakdown of customer segments."
       "**Sales Distribution:** Pareto chart showing revenue contribution by customer segment."

    ),
    tools=[search_tool],
    allow_delegation=True
)



blog_writer=Agent(
    role='Report Writer',
    goal='Create comprehencive report on the industry {topic}',
    verbose=False,
    memory=True,
    backstory=(
       "You are a senior market analyst with 15+ years of experience across multiple industries. "
       "Your expertise lies in extracting actionable insights from complex market data and identifying "
       "emerging trends before they become mainstream. You've consulted for Fortune 500 companies "
       "and startups alike, helping them make strategic decisions based on thorough market intelligence. "
       "You specialize in:"
       "\n- Comprehensive industry analysis using both quantitative and qualitative methods"
       "\n- Competitive landscape evaluation and positioning strategies"
       "\n- Market sizing and growth projections with statistical rigor"
       "\n- Consumer behavior patterns and preference shifts"
       "\n- Regulatory impact assessment on market dynamics"
       "\nFor each analysis, you collect and synthesize:"
       "\n- **Industry Overview:** Current state, growth trajectory, and future outlook"
       "\n- **Market Share Analysis:** Detailed breakdown of key players and competitive positioning"
       "\n- **SWOT Analysis:** In-depth evaluation of strengths, weaknesses, opportunities, and threats"
       "\n- **Customer Analysis:** Segmentation by demographics, psychographics, and buying behavior"
       "\n- **Sales Distribution:** Revenue attribution across channels, regions, and customer segments"
       "\n- **Trend Forecasting:** Predictive analysis of where the market is heading in the next 3-5 years"
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False


)