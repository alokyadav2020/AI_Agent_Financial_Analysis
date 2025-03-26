from crewai import Task
from tools import search_tool
from agents import blog_researcher,blog_writer

## Research Task
# research_task = Task(
#   description=(
#     "Identify the video {topic}."
#     "Get detailed information about the video from the channel video."
#   ),
#   expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
#   tools=[search_tool],
#   agent=blog_researcher,
# )

# # Writing task with language model configuration
# write_task = Task(
#   description=(
#     "get the info from the youtube channel on the topic {topic}."
#   ),
#   expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
#   tools=[search_tool],
#   agent=blog_writer,
#   async_execution=False,
#   output_file='new-blog-post.md'  # Example of output customization
# )
## Research Task
research_task = Task(
  description=(
    "Conduct comprehensive market research on {topic} industry using available online sources."
    "Your research should include:"
    "\n- Industry overview and current market size"
    "\n- Key players and market share analysis"
    "\n- Growth trends and future projections"
    "\n- Regulatory landscape and recent changes"
    "\n- Consumer behavior patterns and preferences"
    "\n- Competitive landscape and positioning strategies"
    "\nUse data from reputable sources including industry reports, financial statements, market analyses, and expert opinions."
  ),
  expected_output='A detailed market research report (800-1000 words) covering industry overview, market share analysis, SWOT analysis, customer segmentation, and sales distribution patterns. Include quantitative data where possible and cite your sources.',
  tools=[search_tool],
  agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Based on the market research provided, create a professional market analysis report on the {topic} industry."
    "Your report should be structured as follows:"
    "\n1. Executive Summary - Highlight key findings and takeaways"
    "\n2. Industry Overview - Current state, size, and growth trajectory"
    "\n3. Market Share Analysis - Key players and their positioning"
    "\n4. SWOT Analysis - Comprehensive evaluation of the industry landscape"
    "\n5. Customer Segmentation - Identify and analyze key customer groups"
    "\n6. Sales Distribution Analysis - Revenue patterns across channels and segments"
    "\n7. Future Outlook - Projected trends and growth opportunities"
    "\n8. Strategic Recommendations - Based on the analysis"
    "\nEnsure the content is data-driven, includes relevant statistics, and delivers actionable insights."
  ),
  expected_output='A polished, comprehensive market analysis report (1500-2000 words) formatted with clear headings, bullet points for key insights, and visual representations of data where appropriate. The report should provide actionable intelligence for strategic decision-making.',
  tools=[search_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'
  
)