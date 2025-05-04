import os
import requests

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Securely fetch from env

def call_llama(cv_text: str, job_role: str, job_desc: str):
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    prompt = f"""
You are a professional CV editor. Here's the original CV:
{cv_text}

Job Role: {job_role}
Job Description: {job_desc}

Modify the CV for this role and return as a JSON with keys like 'summary', 'experience', 'skills', 'projects', etc.
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    result = response.json()
    return {"customized_json": result['choices'][0]['message']['content']}
