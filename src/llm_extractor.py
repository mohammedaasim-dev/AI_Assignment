import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

text = """
OpenAI is an AI company founded in 2015.
"""

prompt = f"""
Extract:
- company
- founded_year

Return JSON only.

{text}
"""

response = model.generate_content(prompt)

print(response.text)