import streamlit as st
from crew import ask
from fpdf import FPDF

# PDF generation function
def save_to_pdf(content, filename="Company_Research_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in content:
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)

# Streamlit app
def main():
    # Set up the main title and introduction
    st.title("AI-Powered Company & Industry Research Assistant")
    st.subheader("Generate insightful research reports and use cases with AI.")
    st.markdown(
        """
        Enter a **company or industry name** to explore key insights, trends, and potential AI-driven applications.
        Use this tool to create a comprehensive report in just a few clicks.
        """
    )

    # Input section with clearer label and a styled text input
    st.markdown("### Enter the Company or Industry Name:")
    question = st.text_input("Company/Industry Name", placeholder="e.g., Fintech, Healthcare, Tesla")

    # Placeholder for storing results in session state
    if 'response' not in st.session_state:
        st.session_state.response = []

    # Submit button with response handling and result display
    if st.button("Generate Insights"):
        # Call the ask function and display the result
        response = ask(question)
        st.session_state.response = [
            f"**Industry Research Report**:\n{response.tasks_output[0].raw}",
            f"**AI Use Cases**:\n{response.tasks_output[1].raw}",
            f"**Resource Collection**:\n{response.tasks_output[2].raw}"
        ]

        # Display results with styled output
        for i, section in enumerate(["Industry Research Report", "AI Use Cases", "Resource Collection"]):
            st.markdown(f"### {section}")
            st.write(st.session_state.response[i])

    # PDF Generation section
    st.markdown("---")
    st.markdown("### Export Your Report")
    st.write("You can save the generated insights as a PDF file for easy sharing and offline access.")

    # Save to PDF button
    if st.button("Save as PDF"):
        save_to_pdf(st.session_state.response)
        st.success("Report saved as PDF successfully!")

    # Download PDF button
    if st.button("Download PDF"):
        with open("Company_Research_Report.pdf", "rb") as pdf_file:
            pdf_data = pdf_file.read()
            st.download_button(
                label="Download PDF Report",
                data=pdf_data,
                file_name="Company_Research_Report.pdf",
                mime="application/pdf"
            )

# Run the app
if __name__ == "__main__":
    main()
