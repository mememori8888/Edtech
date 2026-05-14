# backend/app/repositories/vector_repository.py
import os
from typing import List
from langchain_community.vectorstores import Chroma
# ★ 修正ポイント: langchain_openai は削除し、Googleのみにする
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class VectorRepository:
    """Repositoryパターン: ChromaDBへのアクセスと埋め込み処理を隠蔽"""
    
    def __init__(self, persist_directory: str = "chroma_db"):
        self.persist_directory = persist_directory
        
        # Fail-safe: GeminiのAPIキー未設定を検知して安全に停止
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("環境変数 'GOOGLE_API_KEY' が設定されていません。")
        # backend/app/repositories/vector_repository.py (抜粋)

        # 修正ポイント: モデル名を embedding-001 に変更
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2")
        self.db = Chroma(
            persist_directory=self.persist_directory, 
            embedding_function=self.embeddings
        )

    def add_documents(self, docs: List) -> None:
        try:
            self.db.add_documents(docs)
        except Exception as e:
            print(f"Vector DB Save Error: {e}")

    def similarity_search(self, query: str, k: int = 2) -> List:
        try:
            return self.db.similarity_search(query, k=k)
        except Exception as e:
            print(f"Vector DB Search Error: {e}")
            return []