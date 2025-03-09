import json
import pdfplumber
import spacy
from groq import Groq
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)

def extract_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text.strip()


API_KEY = env("API_KEY")


def analyze_resume(text: str, job_description: str) -> dict:
    prompt = f"""
        You are an AI assistant that analyzes resumes. Given a resume and a job description, extract the following details:
        1. Identify all the skills mentioned in the resume.
        2. Calculate the total years of experience based on the resume.
        3. Categorize the projects based on the domain (e.g. Web Development, Machine Learning, etc.)
        4. Rank the resume relevancy score based on the job description.

        Resume:
        {text}

        Job Description:
        {job_description}
        Provide the output in valid JSON format.
        {{
            "rank":"<percentage>",
            "skills":["skill1","skill2",....],
            "experience":"<years>",
            "project_categories:["category1","category2",....]
        }}
    """

    try:
        client = Groq(api_key=API_KEY)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"},
        )
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        print(f"An error occurred: {e}")


def process_resume(pdf_path, job_description):
    try:
        resume_text = extract_text(pdf_path)
        return analyze_resume(resume_text, job_description)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
