# from crewai import Crew,Process,LLM
# from agents import blog_researcher,blog_writer
# from tasks import research_task,write_task
# from dotenv import load_dotenv
# load_dotenv()
# import os
# os.environ["OPENAI_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")
# os.environ["HUGGINGFACE_API_KEY"] = os.getenv("HUGGINGFACE_API_KEY")
# os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
# # Forming the tech-focused crew with some enhanced configurations
# crew = Crew(
#   agents=[blog_researcher, blog_writer],
#   tasks=[research_task, write_task],
#   process=Process.sequential,  # Optional: Sequential task execution is default
#   memory=True,
#   cache=True,
#   max_rpm=100,
#   share_crew=True
# )

# ## start the task execution process with enhanced feedback
# result=crew.kickoff(inputs={'topic':'Loan Administration, Check Cashing & Other Services in the US - Market Research Report (2014-2029)'})
# print(result)

import streamlit as st
import os
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
st.secrets("HUGGINGFACE_API_KEY")
st.secrets("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv(st.secrets("HUGGINGFACE_API_KEY"))
os.environ["HUGGINGFACE_API_KEY"] = os.getenv(st.secrets("HUGGINGFACE_API_KEY"))
os.environ["SERPER_API_KEY"] = os.getenv(st.secrets("SERPER_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="Market Analysis AI",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Market Analysis AI")
st.markdown("""
Generate comprehensive market analysis reports for any industry using AI agents.
Enter an industry topic below to start the analysis.
""")

# Initialize session state variables
if 'report' not in st.session_state:
    st.session_state.report = ""
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'progress' not in st.session_state:
    st.session_state.progress = 0

# Input for industry topic
topic = st.text_input("Industry Topic", 
                     placeholder="e.g., Electric Vehicles, Cloud Computing, Renewable Energy",
                     disabled=st.session_state.is_running)

# Create tabs for process and results
tab1, tab2 = st.tabs(["Generate Report", "View Report"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("Generate Market Analysis", disabled=st.session_state.is_running or not topic):
            st.session_state.is_running = True
            
            # Progress tracking components
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Update status - Initialization
                status_text.text("Initializing market analysis crew...")
                progress_bar.progress(10)
                time.sleep(1)
                
                # Create crew - same as in your crew.py
                crew = Crew(
                    agents=[blog_researcher, blog_writer],
                    tasks=[research_task, write_task],
                    process=Process.sequential,
                    memory=True,
                    cache=True,
                    max_rpm=100,
                    share_crew=True,

                )
                
                # Update status - Research phase
                status_text.text("Researching market data...")
                progress_bar.progress(30)
                
                # Run the crew
                result = crew.kickoff(inputs={'topic': f"{topic}, US - Market Research Report (2014-2029)"})
                
                # Update status - Completion
                status_text.text("Analysis complete!")
                progress_bar.progress(100)
                
                # Store result
                st.session_state.report = result
                
                # Success message
                st.success(f"Market analysis for '{topic}' completed successfully!")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                
            finally:
                st.session_state.is_running = False
    
    with col2:
        st.markdown("### Analysis Process")
        st.markdown("""
        1. **Market Research** 📚
           - Industry overview and size
           - Key players identification
           - Growth trends analysis
        
        2. **Data Analysis** 📊
           - SWOT analysis
           - Customer segmentation
           - Competitive positioning
        
        3. **Report Generation** 📝
           - Executive summary
           - Strategic insights
           - Future outlook
        """)

with tab2:
    if st.session_state.report:
        st.markdown("## Market Analysis Report")
        st.markdown(f"### Topic: {topic}")
        st.markdown("---")
        
        # Display report
        st.markdown(st.session_state.report)
        
        # Download options
        col1, col2 = st.columns(2)
        with col1:
            if st.download_button(
                label="Download as Markdown",
                data=st.session_state.report,
                file_name=f"market_analysis_{topic.replace(' ', '_').lower()}.md",
                mime="text/markdown"
            ):
                st.success("Report downloaded as Markdown!")
                
        with col2:
            # Create a text file for download
            if st.download_button(
                label="Download as Text",
                data=st.session_state.report,
                file_name=f"market_analysis_{topic.replace(' ', '_').lower()}.txt",
                mime="text/plain"
            ):
                st.success("Report downloaded as Text!")
    else:
        st.info("No report has been generated yet. Use the 'Generate Report' tab to create a market analysis.")

# Sidebar information
with st.sidebar:
    st.markdown("## About Market Analysis AI")
    st.markdown("""
    This application uses AI agents to conduct comprehensive market research and generate 
    detailed analysis reports on any industry.
    
    **Features:**
    - In-depth industry overview
    - Market share analysis
    - SWOT analysis
    - Customer segmentation
    - Sales distribution insights
    - Strategic recommendations
    
    **How it works:**
    The system uses two specialized AI agents:
    1. **Market Researcher** - Collects and analyzes market data
    2. **Report Writer** - Transforms insights into a professional report
    """)
    
    st.markdown("---")
    st.markdown("© 2025 Market Analysis AI")

# Run with: streamlit run app.py