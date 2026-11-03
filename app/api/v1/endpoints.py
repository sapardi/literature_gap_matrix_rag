from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models.schemas import LiteratureItem, SearchQuery, SearchResponse, GenerationResponse
from app.services.rag_service import LITERATURE_DATABASE, search_literature, generate_and_save_outputs

router = APIRouter()

@router.get("/health", summary="Health Check")
def health_check():
    return {"status": "healthy", "service": "JKN Cybersecurity & DLP RAG API"}

@router.get("/literature", response_model=List[LiteratureItem], summary="Get All Literature Database Items")
def get_literature():
    return LITERATURE_DATABASE

@router.post("/rag/search", response_model=SearchResponse, summary="Search Literature via RAG Retriever")
def search_rag(payload: SearchQuery):
    try:
        results = search_literature(payload.query, top_k=payload.top_k)
        return SearchResponse(
            query=payload.query,
            retrieved_count=len(results),
            results=results
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rag/generate", response_model=GenerationResponse, summary="Run RAG Pipeline and Generate Output Files")
def generate_outputs_endpoint():
    try:
        md_path, csv_path, analysis_path = generate_and_save_outputs()
        return GenerationResponse(
            message="RAG pipeline outputs generated successfully",
            markdown_path=md_path,
            csv_path=csv_path,
            analysis_path=analysis_path
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
