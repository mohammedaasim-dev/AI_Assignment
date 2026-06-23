# AI Engineer Trial Assignment

## Overview

This project implements an AI-powered data intelligence pipeline capable of:

- Research paper extraction
- LLM-based information extraction
- Entity resolution
- Startup dataset generation
- Product dataset generation

## Technologies Used

- Python
- Pandas
- Arxiv API
- Gemini API
- RapidFuzz

## Project Structure

AI_Assignment/
├── src/
├── output/
├── data/
├── README.md
└── .gitignore

## Modules

### Research Papers
Extracts AI research papers using Arxiv.

### LLM Extraction
Uses Gemini API to extract structured information.

### Entity Resolution
Maps similar company names to canonical names.

### Startup Dataset
Generates startup records.

### Product Dataset
Generates product records.

## Run

python src/papers.py
python src/paper_extractor.py
python src/entity_resolver.py
python src/startup_generator.py
python src/product_generator.py