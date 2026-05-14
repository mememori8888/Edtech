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
    
    def __init__(self, api_base_url="http://localhost:8000/api/v1"):
        self.api_base_url = api_base_url
        
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEYが設定されていません。")
            
        # 教師役のLLMを初期化 (Geminiのテキスト生成モデル)
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    def generate_integrated_question(self, country_name: str, topic_keyword: str):
        print(f"[{country_name}] のデータと [{topic_keyword}] の知識を収集中...")
        
        # 1. FastAPIから構造化データ(SQLite)を取得
        pop_res = requests.get(f"{self.api_base_url}/population/{country_name}")
        pop_data = pop_res.json() if pop_res.status_code == 200 else "データなし"

        # 2. FastAPIから非構造化データ(Chroma)を取得
        rag_res = requests.post(
            f"{self.api_base_url}/knowledge/search", 
            json={"query": topic_keyword}
        )
        rag_data = rag_res.json().get("results", []) if rag_res.status_code == 200 else "知識なし"

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
    agent = QuestionGeneratorAgent()
    # 日本のデータと、Wikipediaから取り込んだ「人口転換」の知識をぶつける
    question = agent.generate_integrated_question("Japan", "人口転換")
    
    print("================ 生成された問題 ================")
    print(question)
    print("================================================")