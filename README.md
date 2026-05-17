# 🌏 GeoAI-Driven Learning System (GALS)
> **ステータス：Phase 6 (品質保証・CI自動化) 完了 / Phase 7 (本番インフラ刷新・Cloud Run移行) 着手開始**

地理教育における「データ駆動型」の個別最適化学習を実現する、AIエージェント・プラットフォーム。統計データと背景知識を組み合わせ、AIがその場でオリジナル問題を作成します。

---

## 🌐 本番環境 (Deployment)
* **Frontend (UI):** [https://edtech-menk599l8zp3nzsabefzcz.streamlit.app](https://edtech-menk599l8zp3nzsabefzcz.streamlit.app) *(※GCPへ移行予定)*
* **Backend (API):** [https://edtech-wsqi.onrender.com](https://edtech-wsqi.onrender.com) *(※GCPへ移行予定)*

---

## 📊 タスク進行状況 (Roadmap Checklist)

### **✅ 完了済み (Done)**
* **Phase 1: データ基盤の構築**
  - [x] BigQueryからの人口推移データ抽出
  - [x] Pydanticによる厳格なデータ・バリデーションの実装
  - [x] Chroma DBを用いた地理背景知識のベクトル化 (RAG基盤)
* **Phase 2: バックエンドAPI開発**
  - [x] RepositoryパターンによるDBアクセスの隠蔽
  - [x] FastAPIによる統計取得・知識検索エンドポイントの構築
* **Phase 3: AIエージェントの実装**
  - [x] Gemini 2.5 Flashを用いた統合問題生成ロジックと高速化
  - [x] プロンプトエンジニアリングによる「4択問題＋解説」の出力制御
* **Phase 4: UI/UX統合**
  - [x] Streamlitによる対話型インターフェース
  - [x] Plotlyを用いた人口推移の動的グラフ表示
* **Phase 5: 初期本番公開 (PoC)**
  - [x] Render.com (Backend) / Streamlit Cloud (Frontend) へのデプロイ
* **Phase 6: AI品質保証 (QA) & CI/CD自動化**
  - [x] **LangSmith Integration:** 全てのAI実行ログの可視化、1ミリ秒単位のトレース
  - [x] **QA Engineering:** AI特有の「サイレントバグ（エラー文の巻き込み）」を発見・修正
  - [x] **GitHub Actions:** プッシュ時の自動品質テスト(CI)とNGワード検知ゲートの構築
  - [x] **Parameterized Testing:** `pytest` による複数データセットの自動網羅テスト

### **⏳ 進行中 (In Progress)**
* **Phase 7: 本番インフラ刷新 (GCP Migration)**
  - [ ] **Dockerization:** Frontend / Backend のコンテナ化 (Dockerfileの設計)
  - [ ] **Cloud Run Deployment:** コールドスタート問題の解消とゼロスケール運用
  - [ ] **Session Affinity:** StreamlitのWebSocket通信安定化設定

### **📅 今後の予定 (Planned)**
* **Phase 8: 評価基盤と機能拡張**
  - [ ] **Golden Dataset / LLM-as-a-Judge:** LangSmith上での自動採点パイプライン実装
  - [ ] **TypeScript Migration:** フロントエンドのNext.js移行
  - [ ] **User Auth:** 生徒ごとの学習履歴・成績データの保存

---

## 🏗 システムアーキテクチャ
| レイヤー | 技術スタック | 役割 |
| :--- | :--- | :--- |
| **Frontend** | Streamlit (Python) | UI / グラフ表示 (Cloud Runコンテナ稼働予定) |
| **Backend** | FastAPI (Python) | 統計データAPI / ベクトル検索API (Cloud Run稼働予定) |
| **AI Agent** | LangChain / Gemini 2.5 Flash | 知識検索(RAG)とデータ統合、問題生成 |
| **Database** | SQLite / Chroma DB | 構造化統計データ / 非構造化背景知識 |
| **Observability/QA**| **LangSmith / GitHub Actions** | **AI品質の可視化・サイレントバグ監視・自動検品** |

---

## 🛠 設計原則 (Design Principles)
* **KISS (Keep It Simple, Stupid):** プロトタイプはシンプルに、検証は速く。
* **Fail-safe (AI):** AIは無自覚な嘘（ハルシネーション）をつく前提で、CI/CDパイプラインにNGワード検知アサーションを設ける。
* **Observability:** AIの中身をブラックボックスにせず、全てLangSmithで計測しコストとレイテンシを監視する。

---

## 📝 開発ログ
* **2026/05/14:** Phase 5 完了。Render/Streamlit間での本番通信に成功。
* **2026/05/16:** Phase 6 完了。LangSmithを導入し、インフラスリープ時にAIがエラー文を巻き込んで問題生成する「サイレントバグ」を検知。
* **2026/05/16:** GitHub ActionsにてCIパイプラインを構築。異常出力を確実に弾くデジタル検品ラインを稼働。
* **2026/05/17:** Renderのコールドスタートによる待機時間と運用課題を解決するため、Docker + GCP (Cloud Run) へのインフラ移行 (Phase 7) を開始。

---

## 🔄 システム転用・カスタマイズ ガイドライン
本システム（GeoAI-Driven Learning System）は、データベースとプロンプトを差し替えることで、他科目や別ドメインの「AIチューター / アシスタント」として機能するアーキテクチャを採用しています。

別の内容に変更する際は、以下のステップと注意事項を必ず遵守してください。

### 1. 構造化データの入れ替え（SQLite編）
最も重要なのは、AIに確実に参照させたい「事実データ（数値、リスト、マスタデータ）」の再定義です。
* **🚨 注意: Pydanticモデルの厳格化 (Foolproof)**
  `backend/app/models/` 内の型定義を、新しいデータに合わせて必ず書き換えてください。
  * *ダメな例:* `value: str` （何でも入ってしまう）
  * *良い例:* `year: int = Field(..., ge=1868, le=2026)` （歴史データなら年号の範囲を制限する）
  * *理由:* 誤った型や範囲外のデータがDBに入ると、AIがハルシネーション（嘘）をつく原因になります。
* **💡 ヒント: Repositoryパターンの維持**
  `backend/app/repositories/` 内のクラス名は変更しても構いませんが、「DBアクセスを隠蔽する」というインターフェースの役割は絶対に残してください。直接API内にSQLを書かないでください。

### 2. 非構造化データの入れ替え（Chroma DB/RAG編）
AIの「背景知識」となるテキストデータを入れ替えます。
* **🚨 注意: チャンクサイズの再チューニング**
  `scripts/init_vector_db.py` などのチャンキング設定は、ドメインによって最適な値が異なります。
  * *歴史（文脈が長い）:* サイズを大きく（例: `chunk_size=1000`）
  * *英単語や一問一答:* サイズを小さく（例: `chunk_size=200`）
  * *理由:* 意味の区切りが不適切なチャンクが検索でヒットすると、AIの回答が不自然になります。

### 3. エージェント層（APIとプロンプト）の変更
AIに「自分は何者か」と「どのツール（API）を使えるか」を教え直します。
* **🚨 注意: Tool Callingの説明文の明確化 (Fail-safe)**
  AIにツール（FastAPIのエンドポイント）を使わせるための `description` は、極めて具体的に書いてください。
  * *ダメな例:* データベースを検索します。
  * *良い例:* 日本の歴史的な出来事を年号で検索します。引数には西暦(整数)を渡してください。
* **🚨 注意: システムプロンプトの再設定**
  「あなたは◯◯の専門家です」という役割定義を必ず更新してください。また、「わからない場合は『わからない』と答えること」という指示（Fail-safe）は、どのドメインでも残しておくことを推奨します。
