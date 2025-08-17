# lookglass-automation-database
Team 3 – LookGlass Project | Automation &amp; Database

## Overview
This repository contains the backend infrastructure for Team 3 (Automation & Database) of the LookGlass Project. 
The primary goal of this component is to support automated data ingestion, preprocessing, analysis, and structured storage of articles using Python.

## Project Structure
- `src/`: Main source code
  - `common/`: Shared utilities (logging, config loading)
  - `ingestion/`: Fetches articles from external APIs
  - `preprocess/`: Basic text cleaning and filtering
  - `analysis/`: Lightweight keyword-based analysis
  - `db/`: Data models and MongoDB I/O logic
- `tests/`: Simple placeholder for CI-based testing
- `.github/workflows/`: GitHub Actions CI pipeline
- `.env.example`: Template for environment variables

## Status

This repository currently includes:
- Project scaffolding and modular folder structure
- Logging and config loading utilities ???
- Placeholder files for each pipeline stage
- Working GitHub Actions pipeline
- Test placeholder to ensure CI passes

## How to Use

1. Clone the repository
2. Create a `.env` file based on `.env.example`
3. Set up a Python virtual environment
4. Run `python src/runner.py` to execute the pipeline (WIP)
5. Run `pytest` to validate setup

## Next Steps

- Connect to Event Registry API and test real article ingestion
- Test MongoDB saving with sample articles
- Add logic for duplicate filtering, scoring, and relevance tagging
- Extend testing coverage beyond placeholders

## Team HN581
This backend module is maintained by Team HN581: Automation & Database