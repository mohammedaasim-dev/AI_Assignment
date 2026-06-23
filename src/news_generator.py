import pandas as pd
from datetime import datetime

news = []

sources = [
    "OpenAI News",
    "Google AI",
    "Microsoft AI",
    "Anthropic",
    "Hugging Face"
]

for i in range(1000):
    news.append({
        "title": f"AI News Article {i}",
        "source": sources[i % 5],
        "date": datetime.now(),
        "url": f"https://example.com/news/{i}"
    })

df = pd.DataFrame(news)

df.to_csv(
    "output/news.csv",
    index=False
)

print("News dataset created.")