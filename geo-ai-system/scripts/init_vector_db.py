# scripts/init_vector_db.py
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.app.repositories.vector_repository import VectorRepository

# Fail-safe: dotenvが存在しない（または.envファイルがない）環境でも
# OSの環境変数（CodespacesのSecretsなど）を優先して利用する設計
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def setup_vector_db():
    file_path = "data/knowledge/africa_population.md"
    
    # Foolproof: ファイルが存在しない場合は処理を中断
    if not os.path.exists(file_path):
        print(f"エラー: 知識ファイル '{file_path}' が見つかりません。")
        return

    print("ドキュメントを読み込み、ベクトル化を開始します...")
    try:
        # 1. 読み込み
        loader = TextLoader(file_path, encoding='utf-8')
        documents = loader.load()

        # 2. チャンキング (KISS: 最初はシンプルな文字数分割)
        splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        docs = splitter.split_documents(documents)

        # 3. ベクトルDBへ保存
        # ここで VectorRepository が os.getenv("GOOGLE_API_KEY") を呼び出します
        repo = VectorRepository()
        repo.add_documents(docs)
        
        print(f"完了: {len(docs)} 個のチャンクを Chroma DB (chroma_db/) に保存しました！")
    except Exception as e:
        print(f"ベクトルDBの初期化に失敗しました: {e}")

if __name__ == "__main__":
    setup_vector_db()