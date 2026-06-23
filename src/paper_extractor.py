import os
import arxiv
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

client = arxiv.Client()

search = arxiv.Search(
    query="artificial intelligence",
    max_results=100
)

results = []

for paper in client.results(search):

    text = f"""
    Title: {paper.title}

    Summary:
    {paper.summary}
    """

    prompt = f"""
    Extract:
    - research_area
    - short_summary

    Return JSON only.

    {text}
    """

    response = model.generate_content(prompt)

    results.append({
        "title": paper.title,
        "authors": ", ".join(
            [a.name for a in paper.authors]
        ),
        "published": paper.published,
        "paper_url": paper.entry_id,
        "llm_output": response.text
    })

df = pd.DataFrame(results)

df.to_csv(
    "output/paper_analysis.csv",
    index=False
)

print("Analysis completed.")
