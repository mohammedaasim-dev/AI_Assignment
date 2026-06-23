import pandas as pd
from datetime import datetime

jobs = []

companies = [
    "OpenAI",
    "Google",
    "Microsoft",
    "Meta",
    "Anthropic"
]

roles = [
    "AI Engineer",
    "ML Engineer",
    "Data Scientist",
    "Python Developer",
    "LLM Engineer"
]

for i in range(1000):
    jobs.append({
        "schemaVersion": "1.0",
        "recordType": "JOB",
        "company": companies[i % 5],
        "role_family": roles[i % 5],
        "date": datetime.now(),
        "is_remote": True
    })

df = pd.DataFrame(jobs)

df.to_csv(
    "output/jobs.csv",
    index=False
)

print("Jobs dataset created.")