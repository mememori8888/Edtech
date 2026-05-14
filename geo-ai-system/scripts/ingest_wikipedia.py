# scripts/ingest_wikipedia.py
import os
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.app.repositories.vector_repository import VectorRepository

# Fail-safe: Codespaces等の環境変数読み込み用
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def ingest_wikipedia_data():
    # 地理教育に必須のキーワード群（ここを増やせば知識が無限に増えます）
    search_queries = [
        "世界の人口",
        "人口転換",
        "ケッペンの気候区分",
        "日本の地理",
        "世界の農業",
        "都市化"
    ]

    print("Wikipediaから地理の知識を取得し、ベクトル化を開始します...")
    
    # チャンキングの設定 (長文をLLMが飲み込みやすいサイズに分割)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    repo = VectorRepository()
    
    total_chunks = 0

    for query in search_queries:
        print(f"[{query}] の記事を取得中...")
        try:
            # lang="ja" で日本語版Wikipediaを指定。load_max_docs=1 でトップ記事のみ取得 (KISS原則)
            loader = WikipediaLoader(query=query, lang="ja", load_max_docs=1)
            raw_docs = loader.load()
            
            if not raw_docs:
                print(f"  -> 記事が見つかりませんでした。スキップします。")
                continue

            # ドキュメントを分割
            docs = splitter.split_documents(raw_docs)
            
            # メタデータに検索キーワードを付与（後でデバッグしやすくするため）
            for doc in docs:
                doc.metadata["source"] = f"Wikipedia: {query}"
                
            # Chroma DBへ保存
            repo.add_documents(docs)
            total_chunks += len(docs)
            print(f"  -> {len(docs)} 個のチャンクを保存しました。")
            
        except Exception as e:
            # Fail-safe: 一つの記事でエラーが起きても、他の記事の処理を止めない
            print(f"  -> エラーが発生したためスキップします: {e}")

    print(f"\n完了: 合計 {total_chunks} 個のチャンクを Chroma DB に保存しました！")

if __name__ == "__main__":
    ingest_wikipedia_data()