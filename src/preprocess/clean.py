from typing import List, Dict
from src.common.logging import get_logger

logger = get_logger("clean")

def clean_text(text: str) -> str:
    """Trim whitespace and normalize basic text input."""
    return text.strip()

def preprocess_articles(articles: List[Dict]) -> List[Dict]:
    """Lightweight preprocessing: trims title and body."""
    logger.info(f"Preprocessing {len(articles)} articles...")
    cleaned = []

    for article in articles:
        title = clean_text(article.get("title", ""))
        body = clean_text(article.get("body", ""))

        if not title or not body:
            logger.warning("Skipping article with missing title or body.")
            continue

        cleaned.append({
            "title": title,
            "body": body
        })

    return cleaned