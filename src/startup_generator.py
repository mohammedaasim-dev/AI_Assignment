import pandas as pd
from datetime import datetime

startups = []

companies = [
    "OpenAI",
    "Anthropic",
    "Mistral AI",
    "Perplexity",
    "Runway",
    "Cohere",
    "Character AI",
    "Midjourney",
    "Stability AI",
    "Hugging Face",
    "Databricks",
    "Scale AI",
    "Adept AI",
    "Pika Labs",
    "ElevenLabs",
    "Groq",
    "Replit",
    "Harvey AI",
    "Synthesia",
    "Suno"
]

for i in range(1000):
    company = companies[i % len(companies)]

    startups.append({
        "schemaVersion": "1.0",
        "recordType": "STARTUP",
        "source_name": "AI Directory",
        "source_url": f"https://example.com/startup/{i}",
        "entity_name": company,
        "employee_count": (i + 1) * 50,
        "collected_at": datetime.now()
    })

df = pd.DataFrame(startups)

df.to_csv(
    "output/startups.csv",
    index=False
)

print("Startup dataset created.")
print("Total records:", len(df))
