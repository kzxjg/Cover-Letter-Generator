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
    "{job_description} This is the job description, I want you to extract the important skills, job requirements, and what the job entails from the link provided. No preamble"
)

messages = [
    (
        "system",
        "You are a cover letter Generator. You take in the given resumes that the user enters and then outputs a neat cover letter which tailors the cover letter to the resume and job description.",
    ),
    "human", f"{resume_doc}",
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)




