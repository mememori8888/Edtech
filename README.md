🌏 GeoAI-Driven Learning System (GALS)
地理教育における「データ駆動型」の個別最適化学習を実現する、AIエージェント・プラットフォーム。

🚀 プロジェクト概要
本システムは、BigQueryの統計データ（人口・気候・経済等）と最新のLLM（GPT-4/Gemini/Claude）を組み合わせ、生徒一人ひとりの弱点に合わせた「類題作成」と「学習プランニング」を自動化するEdTechソリューションです。

🏗 システムアーキテクチャ
Frontend: Retool / Dify (Low-code Interface)

AI Agent: TypeScript (Node.js, LangChain.js / Vercel AI SDK)

Backend (CP Server): Python (FastAPI)

Database: SQLite (Fact-data), Chroma (Vector DB / RAG)

Data Source: BigQuery (Census Bureau International Population, etc.)

🗺 開発ロードマップ
Phase 1: データ基盤の構築 (Foundation)
[ ] BigQuery Integration: census_bureau_international からの人口推移データの抽出。

[ ] Data Validation Layer: Pydanticを用いた厳格なデータ・バリデーションの実装（Foolproof）。

[ ] RAG Environment: 地理教科書・資料のベクトル化（Chroma DB）と検索基盤の構築。

Phase 2: バックエンドAPI & ロジック開発 (Core Logic)
[ ] Repository Pattern Implementation: DBアクセスの抽象化によるデータソースの隠蔽。

[ ] Dynamic Question Engine: Strategyパターンを用いた「統計推移」や「比較」問題の自動生成ロジック。

[ ] FastAPI Endpoints: エージェントからのTool Callingを受け付けるAPI群の実装。

Phase 3: 自律型AIエージェントの実装 (Intelligence)
[ ] Function Calling Logic: ユーザーの意図に基づき、DB検索とRAGを使い分けるルーティング。

[ ] Planning Strategy: 学習履歴に基づいたパーソナライズ・スケジュール生成アルゴリズム。

[ ] Fail-safe Design: APIエラー時や不適切な入力に対するフォールバック応答の実装。

Phase 4: UI/UX統合と実証テスト (Deployment)
[ ] Frontend Integration: Retool/Dify上での地図UIと対話型インターフェースの結合。

[ ] Prototype Testing: テスター（生徒・教師）によるユーザビリティテストの実施。

[ ] Performance Tuning: プロンプト調整とDBクエリの最適化。

🛠 設計原則 (Design Principles)
Object-Oriented & Patterns: Strategy, Factory, Repository パターンの徹底活用。

Fail-safe: システムの停止を防ぐ例外処理とデフォルト値の定義。

Foolproof: 入力値チェックによる不正操作の完全ガード。

KISS (Keep It Simple, Stupid): 単一責任原則に基づいたシンプルで可読性の高いコード。

📝 開発ログ / メモ
[2026/05/13] プロジェクト発足。データソースとして midyear_population を選定。


[![](https://mermaid.ink/img/pako:eNqtVFtv00gU_iujkZBAck2aSxMshNQmokLKrrpp4YF6H0xjErOJHTmORLaphO2WtrTQbMv9stmWEnrZFipgl4XS_JedTpw8lZ_AGTtNg0jRPuw8jGes833nnO-cM-N4TEvKWMApXcql0UhMVBGsEydQL4-IfY_YW8R-Q-wZYq25h1m6s-rZ5AtXPFBcKsp6Lxr9XFna-R7sZw_H1sULoyJ27lbo3iKxJunUDJyJOV9fur3_6SkxHxFrzrn7sfls5ewV_dzB7kxCNjQtw6GYcrXIoWFDl6VsRjGIuUHM9YPdWRG3yGU1KartHPw86r_ghrBLrPfEeukFdUwKfpbC6v3voDoy6E_JqgFJNKY36N6c83gSYnE2lujC81bII8WcPDymKzmDQz-Cxvy1PAd-1FQ0LSkq3I4PO8Cj6BCx3rEA7DI6DYpOuufN-kJ5f-_JMfEH0Oi_jx8dvF_4LwQdqSQVXR4zFE1FIwMdCQ6xGsHe5oG9ldtQ0UhrKofOS3kDLDozYet8QXX58kBAtyuN5fn6eqVhfxIYnG5VndoisR8Qe90Vdo7t1mvPBGJtLv_eXJ6HPqjPlL2fX5GDP9TT03PkpJuCQR4l-geJ_ZHY024Za8doFmQ1f_lHd0BXjeKJo7-XYgOjJ0VMbGjYV6zb7c3YQEujaFrXspKzNeuqc6qDK3GI2iD2n66zv4kNTXarEz78U1wx5G7wePyHkwCHT8t0cGikJ9i2PNVNj-aN5_XyB7B1Kiv09mtmqXpzCFqeKxG76sbxF9vNbTr1gt56QqzF5g0TJrHkNbuHcI8uiNamGlWTmJu0BiP7kJhV-hug39DpDzDBrdgOq4SiUiajqCnwXGIl9MjaNXQJ66tPnbcrbNr7B8EOHgZG0i7Ifu0Z3QI320w4kBsG1PoHRC-xMvyvfIlDvlay_DcSrTGVXu011negZep31hqb90usMN-EwaD03kK7ob0XC9Dw4MGVTled8k0Xijl4g5UkFgy9IHM4K-tZiV3xOCMVsZGWs7KIBTgmJf0XEYvqBGByknpZ07KHMF0rpNJYuCpl8nAr5JKSIccUCTr-yARaQ9ajWkE1sOAPuRRYGMfXsRAIhfiQzxcJ-8N9Z8IBfyTI4SIWQj6-LxIOhgORSKS31xc80zfB4V9drz4-Eg5NfAEJxNgJ?type=png)](https://mermaid.live/edit#pako:eNqtVFtv00gU_iujkZBAck2aSxMshNQmokLKrrpp4YF6H0xjErOJHTmORLaphO2WtrTQbMv9stmWEnrZFipgl4XS_JedTpw8lZ_AGTtNg0jRPuw8jGes833nnO-cM-N4TEvKWMApXcql0UhMVBGsEydQL4-IfY_YW8R-Q-wZYq25h1m6s-rZ5AtXPFBcKsp6Lxr9XFna-R7sZw_H1sULoyJ27lbo3iKxJunUDJyJOV9fur3_6SkxHxFrzrn7sfls5ewV_dzB7kxCNjQtw6GYcrXIoWFDl6VsRjGIuUHM9YPdWRG3yGU1KartHPw86r_ghrBLrPfEeukFdUwKfpbC6v3voDoy6E_JqgFJNKY36N6c83gSYnE2lujC81bII8WcPDymKzmDQz-Cxvy1PAd-1FQ0LSkq3I4PO8Cj6BCx3rEA7DI6DYpOuufN-kJ5f-_JMfEH0Oi_jx8dvF_4LwQdqSQVXR4zFE1FIwMdCQ6xGsHe5oG9ldtQ0UhrKofOS3kDLDozYet8QXX58kBAtyuN5fn6eqVhfxIYnG5VndoisR8Qe90Vdo7t1mvPBGJtLv_eXJ6HPqjPlL2fX5GDP9TT03PkpJuCQR4l-geJ_ZHY024Za8doFmQ1f_lHd0BXjeKJo7-XYgOjJ0VMbGjYV6zb7c3YQEujaFrXspKzNeuqc6qDK3GI2iD2n66zv4kNTXarEz78U1wx5G7wePyHkwCHT8t0cGikJ9i2PNVNj-aN5_XyB7B1Kiv09mtmqXpzCFqeKxG76sbxF9vNbTr1gt56QqzF5g0TJrHkNbuHcI8uiNamGlWTmJu0BiP7kJhV-hug39DpDzDBrdgOq4SiUiajqCnwXGIl9MjaNXQJ66tPnbcrbNr7B8EOHgZG0i7Ifu0Z3QI320w4kBsG1PoHRC-xMvyvfIlDvlay_DcSrTGVXu011negZep31hqb90usMN-EwaD03kK7ob0XC9Dw4MGVTled8k0Xijl4g5UkFgy9IHM4K-tZiV3xOCMVsZGWs7KIBTgmJf0XEYvqBGByknpZ07KHMF0rpNJYuCpl8nAr5JKSIccUCTr-yARaQ9ajWkE1sOAPuRRYGMfXsRAIhfiQzxcJ-8N9Z8IBfyTI4SIWQj6-LxIOhgORSKS31xc80zfB4V9drz4-Eg5NfAEJxNgJ)
