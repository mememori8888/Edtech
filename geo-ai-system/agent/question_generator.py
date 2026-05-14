# agent/question_generator.py
import os
import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Fail-safe: 環境変数の読み込み
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class QuestionGeneratorAgent:
    """Strategyパターン: 異なるデータソースを組み合わせて問題を作成するエージェント"""
    
    # 修正ポイント: デフォルトのURLをRenderの本番URLに変更
    def __init__(self, api_base_url="https://edtech-wsqi.onrender.com/api/v1"):
        self.api_base_url = api_base_url
        
        if not os.getenv("GOOGLE_API_KEY"):
            # Streamlit CloudのSecretsから取得される想定
            raise ValueError("GOOGLE_API_KEYが設定されていません。")
            
        # 教師役のLLMを初期化 (Gemini 1.5 Flashを使用)
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    def generate_integrated_question(self, country_name: str, topic_keyword: str):
        print(f"[{country_name}] のデータと [{topic_keyword}] の知識を収集中...")
        
        # 1. FastAPI(Render上の本番サーバー)から構造化データ(SQLite)を取得
        try:
            pop_res = requests.get(f"{self.api_base_url}/population/{country_name}", timeout=10)
            pop_data = pop_res.json() if pop_res.status_code == 200 else "データなし"
        except Exception as e:
            pop_data = f"データ取得エラー: {e}"

        # 2. FastAPI(Render上の本番サーバー)から非構造化データ(Chroma)を取得
        try:
            rag_res = requests.post(
                f"{self.api_base_url}/knowledge/search", 
                json={"query": topic_keyword},
                timeout=10
            )
            rag_data = rag_res.json().get("results", []) if rag_res.status_code == 200 else "知識なし"
        except Exception as e:
            rag_data = f"知識取得エラー: {e}"

        # 3. プロンプトの組み立て (生成ロジック)
        prompt = PromptTemplate.from_template("""
        あなたは優秀な高校地理の先生です。
        以下の【人口推移データ】と【背景知識】の両方を組み合わせて、生徒の思考力を問う「4択問題」を1問だけ作成してください。

        【人口推移データ】(事実として扱うこと)
        {pop_data}

        【背景知識】(解説の根拠として扱うこと)
        {rag_data}

        以下のフォーマットで出力してください。
        ---
        【問題】(ここに問題文)
        1. (選択肢1)
        2. (選択肢2)
        3. (選択肢3)
        4. (選択肢4)
        
        【正解】(番号)
        【解説】(データと背景知識を必ず紐づけて解説すること)
        ---
        """)

        # 4. LLMに思考させる
        print("AIが問題を構築中...\n")
        chain = prompt | self.llm
        response = chain.invoke({
            "pop_data": pop_data,
            "rag_data": rag_data
        })
        
        return response.content

# 実行ブロック
if __name__ == "__main__":
    # 本番環境への接続テスト
    agent = QuestionGeneratorAgent()
    question = agent.generate_integrated_question("Japan", "人口転換")
    
    print("================ 生成された問題 ================")
    print(question)
    print("================================================")