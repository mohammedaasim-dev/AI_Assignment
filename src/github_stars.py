import requests
import pandas as pd

df = pd.read_csv("output/research_papers.csv")

stars = []

for index, row in df.head(10).iterrows():
    github_url = ""

    stars.append({
        "paper": row["title"],
        "github_url": github_url,
        "stars": 0
    })

result = pd.DataFrame(stars)

result.to_csv("output/github_stars.csv", index=False)

print("GitHub data saved.")