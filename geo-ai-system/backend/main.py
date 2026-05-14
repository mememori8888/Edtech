# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.app.repositories.population_repository import PopulationRepository
from backend.app.repositories.vector_repository import VectorRepository

app = FastAPI(title="GeoAI-Driven Learning System API")

# Factory的にインスタンスを生成
pop_repo = PopulationRepository()
vec_repo = VectorRepository()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "GeoAI API is running!"}

# --- 1. 構造化データの取得API (SQLite) ---
@app.get("/api/v1/population/{country_name}")
def get_population(country_name: str):
    data = pop_repo.get_by_country(country_name)
    # Foolproof: データが存在しない場合は適切なHTTPステータスを返す
    if not data:
        raise HTTPException(status_code=404, detail=f"{country_name} のデータが見つかりません。")
    return {"country": country_name, "data": data}

# --- 2. 非構造化データの検索API (RAG/Chroma) ---
class SearchQuery(BaseModel):
    query: str

@app.post("/api/v1/knowledge/search")
def search_knowledge(request: SearchQuery):
    """Fail-safe: 検索結果がゼロでもエラーにせず空リストを返す"""
    docs = vec_repo.similarity_search(request.query)
    return {
        "query": request.query,
        "results": [doc.page_content for doc in docs]
    }