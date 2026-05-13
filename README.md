# Edtech

graph TD
    subgraph Frontend [フロントエンド]
        UI[ローコードUI / ユーザー画面<br>例: Streamlit, Dify, Retool]
    end

    subgraph Agent [AIエージェント層]
        TS[TypeScript AIエージェント<br>LangChain.js / Vercel AI SDK]
    end

    subgraph Backend [CPサーバ / ツール提供層]
        API[Python FastAPI<br>ツール呼び出し受付]
        Plan[学習プランニング機能]
        Quiz[類題作成機能]
    end

    subgraph RAG_System [RAG・データ層]
        VDB[(ベクトルDB<br>Chroma / FAISS)]
        DB[(生徒データDB<br>SQLite等)]
        LLM((LLM<br>OpenAI / Claude / Gemini))
    end

    %% データの流れ
    UI <-->|チャット / リクエスト| TS
    TS <-->|Function Calling| API
    TS <-->|推論・計画| LLM
    API --> Plan
    API --> Quiz
    Quiz -->|関連知識の検索| VDB
    Plan -->|成績取得・更新| DB
    API <-->|回答生成| LLM
