import arxiv
import pandas as pd

papers = []

client = arxiv.Client()

search = arxiv.Search(
    query="artificial intelligence",
    max_results=100,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

for paper in client.results(search):
    papers.append({
        "title": paper.title,
        "authors": ", ".join(
            [author.name for author in paper.authors]
        ),
        "published": paper.published,
        "url": paper.entry_id
    })

df = pd.DataFrame(papers)

df.to_csv("output/research_papers.csv", index=False)

print("Research papers saved successfully!")
print("Total papers:", len(df))