# Multi-Agent Market Research and Use Case Generation System

This project is a multi-agent system designed to conduct in-depth market research and generate AI/ML use cases for a target company within a specific industry. Using Google Generative AI, CrewAI, and Streamlit for an interactive user interface, this system enables quick, automated research and report generation through specialized agents.

## Project Overview

This system leverages four main agents to complete distinct tasks:
1. **Research Agent** - Gathers industry insights and competitor analysis for the target company.
2. **Use Case Generation Agent** - Proposes relevant AI/ML and Generative AI applications based on research findings.
3. **Resource Collection Agent** - Identifies suitable datasets from platforms like Kaggle, HuggingFace, and GitHub for suggested use cases.
4. **Report Generation Agent** - Compiles all findings into a detailed report ready for decision-making.

## Key Features

- **Automated Market Research**: Collects and analyzes industry and company information.
- **AI/ML Use Case Recommendations**: Generates actionable AI/ML use cases tailored to the industry and company’s goals.
- **Dataset Search**: Locates relevant datasets to support the use cases.
- **Report Generation**: Compiles a comprehensive report, downloadable in plain text format.
- **Streamlit Interface**: Interactive web interface for easy input and real-time feedback.

## Technology Stack

- **Python**: Core programming language.
- **Streamlit**: Web framework for the UI.
- **CrewAI**: Task orchestration and agent management.
- **Google Generative AI**: Provides the underlying generative model.
- **dotenv**: Manages environment variables.
- **SerperDevTool**: Used for Google searches (optional).

## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine.
   ```bash
   git clone [https://github.com/jindalayush326/Multi_Agent_Market_Research_System.git]
   ```

2. Navigate to the project directory.
   ```bash
   cd Multi_Agent_Market_Research_System
   ```

3. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

Set up API keys:

4. Create a .env file in the root directory and add your API keys for Google Gemini Flash 1.5 and SerperAPI as follows:
   GOOGLE_API_KEY=<your-google-api-key>
   SERPER_API_KEY=<your-serper-api-key>

## Usage

1. Ensure you have installed all dependencies as instructed above.

2. Run the Streamlit app.
   ```bash
   streamlit run app.py
   ```

3. Access the app through your browser at http://localhost:8501

4. Interact with the app:

   Enter the name of the company and the relevant industry (e.g.,Tech, Health, Automotive, Finance, Retail).
   The app will generate a detailed financial and market research report, including AI use cases and relevant datasets. 
