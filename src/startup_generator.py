import pandas as pd
from datetime import datetime

startups = []

companies = [
    "OpenAI",
    "Anthropic",
    "Perplexity",
    "Mistral AI",
    "Cohere",
    "Runway",
    "Midjourney",
    "Hugging Face",
    "Stability AI",
    "Character AI"
]

for i in range(100):
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
