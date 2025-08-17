from dataclasses import dataclass, field
from typing import List

@dataclass
class Article:
    title: str
    body: str
    url: str
    date: str
    source: str
    lang: str = "eng"
    has_keywords: List[str] = field(default_factory=list)
    is_long: bool = False
    score: float = 0.0
    word_count: int = 0