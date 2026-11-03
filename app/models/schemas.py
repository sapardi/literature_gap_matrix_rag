from pydantic import BaseModel
from typing import List, Optional

class LiteratureItem(BaseModel):
    id: str
    paper: str
    doi: str
    problem: str
    metode: str
    dataset: str
    temuans: str
    keterbatasan: str
    future_work: str

class SearchQuery(BaseModel):
    query: str = "Keamanan siber Data Loss Prevention RAG Jaminan Kesehatan Nasional data pribadi kesehatan"
    top_k: int = 8

class SearchResponse(BaseModel):
    query: str
    retrieved_count: int
    results: List[LiteratureItem]

class GenerationResponse(BaseModel):
    message: str
    markdown_path: str
    csv_path: str
    analysis_path: str
