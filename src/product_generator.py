import pandas as pd
from datetime import datetime

products = []

product_names = [
    "ChatGPT",
    "Claude",
    "Gemini",
    "Perplexity AI",
    "Midjourney",
    "Stable Diffusion",
    "Copilot",
    "Character AI",
    "Runway Gen",
    "Mistral Chat"
]

companies = [
    "OpenAI",
    "Anthropic",
    "Google",
    "Perplexity",
    "Midjourney",
    "Stability AI",
    "Microsoft",
    "Character AI",
    "Runway",
    "Mistral AI"
]

pricing = [
    "FREE",
    "FREEMIUM",
    "PAID",
    "ENTERPRISE"
]

for i in range(100):
    products.append({
        "schemaVersion": "1.0",
        "recordType": "PRODUCT",
        "source_name": "AI Product Directory",
        "source_url": f"https://example.com/product/{i}",
        "startup_name": companies[i % len(companies)],
        "product_name": product_names[i % len(product_names)],
        "pricing_model": pricing[i % len(pricing)],
        "collected_at": datetime.now()
    })

df = pd.DataFrame(products)

df.to_csv(
    "output/products.csv",
    index=False
)

print("Product dataset created.")
print("Total products:", len(df))