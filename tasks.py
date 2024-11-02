from crewai import Task
from agents import industry_researcher, use_case_generator, resource_collector

# Task for Industry Research Agent
industry_research_task = Task(
    description=(
        "Research and analyze the company/industry: {company}. "
        "Begin by gathering information using the appropriate tools with correctly formatted inputs. "
        "Identify key offerings, strategic areas of focus, and the market position of the company. "
        "Provide a comprehensive overview of the industry landscape, covering major competitors, current trends, and challenges. "
        "Use all necessary tools first to collect the research data before summarizing. "
        "Finally, deliver a detailed, insightful report on {company}'s market position and industry outlook."
    ),
    expected_output=(
        "After completing your research using the tools with correct input formats, provide a detailed report for {company} that includes:\n"
        "1. A high-level overview of the company/industry\n"
        "2. Key products and services\n"
        "3. Strategic areas of focus\n"
        "4. Major industry competitors\n"
        "5. Current market trends\n"
        "6. Industry challenges and growth opportunities"
    ),
    agent=industry_researcher
)

# Task for Market Standards & Use Case Generation Agent
use_case_generation_task = Task(
    description=(
        "Based on insights from the industry research task, explore current trends in Generative AI and AI/ML for this specific domain or industry. "
        "Utilize various sources such as internet searches, reading relevant articles, and scanning documents (ensure you use the correct tool and format for each). "
        "Develop a list of 4-5 relevant use cases demonstrating how {company} could leverage GenAI, LLMs, and ML technologies to improve processes or offer new services. "
        "For each use case, include the objective, AI application, and cross-functional benefits. "
        "Specify implementation possibilities by referencing relevant frameworks or libraries. Use tools to find supporting information first, and return a structured list only after completing the research."
    ),
    expected_output=(
        "After researching thoroughly, return a list of 4-5 GenAI, LLM, and ML use cases for {company}. Each use case should include:\n"
        "1. A brief description of the use case (2-3 lines)\n"
        "2. The objective of the use case\n"
        "3. How the use case could be implemented, including potential libraries, frameworks, or methodologies\n"
        "4. Cross-functional benefits across departments"
    ),
    agent=use_case_generator
)

# Task for Resource Asset Collector Agent
resource_collection_task = Task(
    description=(
        "For each Generative AI or AI/ML use case identified for {company}, find relevant resources like datasets, tools, or libraries that could support implementation. "
        "Use platforms such as Kaggle, Hugging Face, and GitHub to search for applicable resources (be careful not to download or scrape large datasets; assess relevance based on titles and descriptions). "
        "Return only actual links that are found via the search tool – avoid creating any links manually. "
        "Focus on finding 2-3 quality resources per use case to guide the implementation effectively."
    ),
    expected_output=(
        "After compiling resources using the tools with correct inputs, provide a curated list of top use cases that includes:\n"
        "1. A short description of each use case and its potential impact\n"
        "2. Implementation insights (how the use case could be set up)\n"
        "3. Relevant resources and references (2-3 per use case)"
    ),
    agent=resource_collector
)
