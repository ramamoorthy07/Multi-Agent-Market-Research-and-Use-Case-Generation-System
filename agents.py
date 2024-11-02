# Import necessary libraries
from crewai import Agent, LLM
import os 
from dotenv import load_dotenv
from tools import search_tool, scrape_tool, pdf_tool

# Load environment variables from .env file
load_dotenv()

# Retrieve the Together API key from environment variables
together_api_key = os.getenv('TOGETHER_API_KEY')

if not together_api_key:
    raise ValueError("API key not found. Please set TOGETHER_API_KEY in your .env file.")

# Initialize the LLM
try:
    llm = LLM(
        model='openai/Qwen/Qwen2.5-72B-Instruct-Turbo',
        api_key=together_api_key,
        api_base='https://api.together.xyz'
    )
except Exception as e:
    print(f"Error initializing LLM: {e}")
    exit(1)

# Enhanced Agent 1: Industry Researcher Agent
industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="""Conduct a comprehensive analysis of the {company} industry sector to identify 
    current market trends, competitor strategies, and unique positioning opportunities 
    for {company}. Focus on key offerings, recent advancements, strategic focus areas, 
    and high-potential growth areas in the industry.""",
    backstory="""As an experienced industry analyst, you specialize in quickly assessing 
    the competitive landscape and identifying strategic opportunities. Your insights 
    are highly valuable for decision-makers aiming to enhance competitive positioning 
    and strategic alignment within the industry.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_iter=20
)

# Enhanced Agent 2: AI Use Case Strategist
use_case_generator = Agent(
    role="AI Use Case Strategist",
    goal="""Research current and emerging industry trends within {company}'s domain, 
    identifying cutting-edge applications of AI and ML that could provide competitive 
    advantages. Generate innovative, practical use cases tailored to business needs, 
    emphasizing efficiency, scalability, and potential ROI.""",
    backstory="""With expertise in GenAI, AI, and ML, you excel at translating 
    technological advancements into practical, transformative business solutions. 
    You bridge the gap between innovation and application, recommending use cases 
    that drive tangible value and meet emerging market demands.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool, pdf_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20
)

# Enhanced Agent 3: Resource Asset Collector
resource_collector = Agent(
    role="AI Resource Specialist",
    goal="""Identify and compile a curated set of high-quality datasets, libraries, 
    and AI/ML tools essential for implementing the proposed AI use cases for {company}. 
    Ensure that resources are relevant to the specific industry and practical for 
    seamless integration into real-world applications.""",
    backstory="""An AI resource expert, you leverage your vast knowledge of AI and ML 
    tools, datasets, and libraries to source tailored resources that align with the 
    strategic goals of a project. Your expertise ensures that each recommended resource 
    is practical, scalable, and aligned with industry standards.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20  
)

# Debugging: Print success messages
print("Agents created successfully.")
