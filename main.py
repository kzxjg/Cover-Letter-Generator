import os
import sys

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from docx import Document

import getpass


if len(sys.argv) < 3:
    sys.exit(1)

resume = sys.argv[1]
job_description = sys.argv[2]

loader = WebBaseLoader(job_description)

resume_doc = Document(resume)

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

job_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in extracting important information from a job description."),
        ("human", ". No preamble. Extract the key requirements from this job description such as the role requirements, education requirements, YOE, and what the role entails"),
        ("human", f"Job Description: {job_description}")
    ]
)
extract_job = job_prompt | llm
job_response = extract_job.invoke({})
job_details = job_response.content

cover_letter_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", "You are a cover letter generator which generates a cover letter based on the resume that is provided", 
            "Generate a cover letter based on the extracted job details and tailor it to the resume that I have provided",
        ),
        ("human", f"My Resume:\n{resume_doc}\n\nJob Details:\n{job_details}\n\nPlease generate a professional cover letter."),
    ]
)

CV_extract = cover_letter_prompt | llm
ai_msg = CV_extract.inovke({})
print(ai_msg.content)









