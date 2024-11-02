from crewai_tools import ScrapeWebsiteTool, SerperDevTool,PDFSearchTool
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['SERPER_API_KEY']=os.getenv('SERPER_API_KEY')
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

pdf_tool = PDFSearchTool(
    
    
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-flash-002",

            ),
        ),
        embedder=dict(
            provider="google", 
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    ),
    pdf='.\report.pdf')


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()