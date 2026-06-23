from rapidfuzz import process
import pandas as pd

known_companies = [
    "OpenAI",
    "Anthropic",
    "Google DeepMind",
    "Meta AI",
    "Hugging Face",
    "Perplexity"
]

test_names = [
    "Open AI",
    "OpenAI Inc",
    "Google Deepmind",
    "MetaAI",
    "HuggingFace"
]

results = []

for name in test_names:
    match = process.extractOne(name, known_companies)

    results.append({
        "raw_name": name,
        "canonical_name": match[0],
        "score": round(match[1], 2)
    })

df = pd.DataFrame(results)

df.to_csv(
    "output/entity_mapping.csv",
    index=False
)

print(df)
print("\nEntity mapping saved successfully.")