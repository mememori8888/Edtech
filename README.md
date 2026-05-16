# 🌏 GeoAI-Driven Learning System (GALS)
> **ステータス：Phase 5 (本番デプロイ) 完了 / Phase 6 (品質保証) 着手開始**

地理教育における「データ駆動型」の個別最適化学習を実現する、AIエージェント・プラットフォーム。統計データと背景知識を組み合わせ、AIがその場でオリジナル問題を作成します。

---

## 🌐 本番環境 (Deployment)
* **Frontend (UI):** [https://edtech-menk599l8zp3nzsabefzcz.streamlit.app](https://edtech-menk599l8zp3nzsabefzcz.streamlit.app)
* **Backend (API):** [https://edtech-wsqi.onrender.com](https://edtech-wsqi.onrender.com)

---

## 📊 タスク進行状況 (Roadmap Checklist)

### **✅ 完了済み (Done)**
* **Phase 1: データ基盤の構築**
  - [x] BigQuery(census_bureau_international)からの人口推移データ抽出
  - [x] Pydanticによる厳格なデータ・バリデーションの実装
  - [x] Chroma DBを用いた地理背景知識のベクトル化 (RAG基盤)
* **Phase 2: バックエンドAPI開発**
  - [x] RepositoryパターンによるDBアクセスの隠蔽
  - [x] FastAPIによる統計取得・知識検索エンドポイントの構築
* **Phase 3: AIエージェントの実装**
  - [x] Gemini 1.5 Flashを用いた統合問題生成ロジック
  - [x] プロンプトエンジニアリングによる「4択問題＋解説」の出力制御
* **Phase 4: UI/UX統合**
  - [x] Streamlitによる対話型インターフェース
  - [x] Plotlyを用いた人口推移の動的グラフ表示
* **Phase 5: システム本番公開**
  - [x] Render.com (Backend) へのデプロイと環境変数設定
  - [x] Streamlit Cloud (Frontend) へのデプロイとSecrets管理
  - [x] 開発・本番環境でのパス解決ロジックの実装

### **⏳ 進行中 (In Progress)**
* **Phase 6: AI品質保証 (QA) & CI自動化**
  - [ ] **LangSmith Integration:** 全てのAI実行ログの可視化とトレース
  - [ ] **Golden Dataset:** 評価基準となる「良質な問題セット」の作成
  - [ ] **LLM-as-a-Judge:** 生成問題の自動採点(Accuracy/Complexity)の実装
  - [ ] **GitHub Actions:** プッシュ時の自動品質テスト(CI)の構築

### **📅 今後の予定 (Planned)**
* **Phase 7: 堅牢化とプロダクト化**
  - [ ] **TypeScript Migration:** フロントエンドのNext.js移行
  - [ ] **Schema-first Development:** OpenAPIによる型定義の自動生成
* **Phase 8: 機能拡張**
  - [ ] **User Auth:** 生徒ごとの学習履歴・成績データの保存
  - [ ] **Multimodal:** 地図や図表画像を読み解く問題生成への対応

---

## 🏗 システムアーキテクチャ
| レイヤー | 技術スタック | 役割 |
| :--- | :--- | :--- |
| **Frontend** | Streamlit (Python) | UI / グラフ表示 (将来的にTypeScript/Next.jsへ) |
| **Backend** | FastAPI (Python) | 統計データAPI / ベクトル検索API |
| **AI Agent** | LangChain / Gemini | 知識検索(RAG)とデータ統合、問題生成 |
| **Database** | SQLite / Chroma DB | 構造化統計データ / 非構造化背景知識 |
| **Observability**| **LangSmith** | **AI品質モニタリング・自動評価** |

---

## 🛠 設計原則 (Design Principles)
* **KISS (Keep It Simple, Stupid):** プロトタイプはシンプルに、検証は速く。
* **Fail-safe:** APIエラーやAIのハルシネーションに対する防御策を常に用意する。
* **Observability:** AIの中身をブラックボックスにせず、全てLangSmithで計測する。

---

## 📝 開発ログ
* **2026/05/14:** Phase 5 完了。Render/Streamlit間での本番通信に成功。
* **2026/05/14:** 「再起動(Reboot)」により、デプロイ時のモジュール読み込みキャッシュ問題を解決。
* **2026/05/14:** Phase 6 (LangSmith導入) への移行を決定。


[![](https://mermaid.ink/img/pako:eNqtVFtv00gU_iujkZBAck2aSxMshNQmokLKrrpp4YF6H0xjErOJHTmORLaphO2WtrTQbMv9stmWEnrZFipgl4XS_JedTpw8lZ_AGTtNg0jRPuw8jGes833nnO-cM-N4TEvKWMApXcql0UhMVBGsEydQL4-IfY_YW8R-Q-wZYq25h1m6s-rZ5AtXPFBcKsp6Lxr9XFna-R7sZw_H1sULoyJ27lbo3iKxJunUDJyJOV9fur3_6SkxHxFrzrn7sfls5ewV_dzB7kxCNjQtw6GYcrXIoWFDl6VsRjGIuUHM9YPdWRG3yGU1KartHPw86r_ghrBLrPfEeukFdUwKfpbC6v3voDoy6E_JqgFJNKY36N6c83gSYnE2lujC81bII8WcPDymKzmDQz-Cxvy1PAd-1FQ0LSkq3I4PO8Cj6BCx3rEA7DI6DYpOuufN-kJ5f-_JMfEH0Oi_jx8dvF_4LwQdqSQVXR4zFE1FIwMdCQ6xGsHe5oG9ldtQ0UhrKofOS3kDLDozYet8QXX58kBAtyuN5fn6eqVhfxIYnG5VndoisR8Qe90Vdo7t1mvPBGJtLv_eXJ6HPqjPlL2fX5GDP9TT03PkpJuCQR4l-geJ_ZHY024Za8doFmQ1f_lHd0BXjeKJo7-XYgOjJ0VMbGjYV6zb7c3YQEujaFrXspKzNeuqc6qDK3GI2iD2n66zv4kNTXarEz78U1wx5G7wePyHkwCHT8t0cGikJ9i2PNVNj-aN5_XyB7B1Kiv09mtmqXpzCFqeKxG76sbxF9vNbTr1gt56QqzF5g0TJrHkNbuHcI8uiNamGlWTmJu0BiP7kJhV-hug39DpDzDBrdgOq4SiUiajqCnwXGIl9MjaNXQJ66tPnbcrbNr7B8EOHgZG0i7Ifu0Z3QI320w4kBsG1PoHRC-xMvyvfIlDvlay_DcSrTGVXu011negZep31hqb90usMN-EwaD03kK7ob0XC9Dw4MGVTled8k0Xijl4g5UkFgy9IHM4K-tZiV3xOCMVsZGWs7KIBTgmJf0XEYvqBGByknpZ07KHMF0rpNJYuCpl8nAr5JKSIccUCTr-yARaQ9ajWkE1sOAPuRRYGMfXsRAIhfiQzxcJ-8N9Z8IBfyTI4SIWQj6-LxIOhgORSKS31xc80zfB4V9drz4-Eg5NfAEJxNgJ?type=png)](https://mermaid.live/edit#pako:eNqtVFtv00gU_iujkZBAck2aSxMshNQmokLKrrpp4YF6H0xjErOJHTmORLaphO2WtrTQbMv9stmWEnrZFipgl4XS_JedTpw8lZ_AGTtNg0jRPuw8jGes833nnO-cM-N4TEvKWMApXcql0UhMVBGsEydQL4-IfY_YW8R-Q-wZYq25h1m6s-rZ5AtXPFBcKsp6Lxr9XFna-R7sZw_H1sULoyJ27lbo3iKxJunUDJyJOV9fur3_6SkxHxFrzrn7sfls5ewV_dzB7kxCNjQtw6GYcrXIoWFDl6VsRjGIuUHM9YPdWRG3yGU1KartHPw86r_ghrBLrPfEeukFdUwKfpbC6v3voDoy6E_JqgFJNKY36N6c83gSYnE2lujC81bII8WcPDymKzmDQz-Cxvy1PAd-1FQ0LSkq3I4PO8Cj6BCx3rEA7DI6DYpOuufN-kJ5f-_JMfEH0Oi_jx8dvF_4LwQdqSQVXR4zFE1FIwMdCQ6xGsHe5oG9ldtQ0UhrKofOS3kDLDozYet8QXX58kBAtyuN5fn6eqVhfxIYnG5VndoisR8Qe90Vdo7t1mvPBGJtLv_eXJ6HPqjPlL2fX5GDP9TT03PkpJuCQR4l-geJ_ZHY024Za8doFmQ1f_lHd0BXjeKJo7-XYgOjJ0VMbGjYV6zb7c3YQEujaFrXspKzNeuqc6qDK3GI2iD2n66zv4kNTXarEz78U1wx5G7wePyHkwCHT8t0cGikJ9i2PNVNj-aN5_XyB7B1Kiv09mtmqXpzCFqeKxG76sbxF9vNbTr1gt56QqzF5g0TJrHkNbuHcI8uiNamGlWTmJu0BiP7kJhV-hug39DpDzDBrdgOq4SiUiajqCnwXGIl9MjaNXQJ66tPnbcrbNr7B8EOHgZG0i7Ifu0Z3QI320w4kBsG1PoHRC-xMvyvfIlDvlay_DcSrTGVXu011negZep31hqb90usMN-EwaD03kK7ob0XC9Dw4MGVTled8k0Xijl4g5UkFgy9IHM4K-tZiV3xOCMVsZGWs7KIBTgmJf0XEYvqBGByknpZ07KHMF0rpNJYuCpl8nAr5JKSIccUCTr-yARaQ9ajWkE1sOAPuRRYGMfXsRAIhfiQzxcJ-8N9Z8IBfyTI4SIWQj6-LxIOhgORSKS31xc80zfB4V9drz4-Eg5NfAEJxNgJ)


🔄 システム転用・カスタマイズ ガイドライン
本システム（GeoAI-Driven Learning System）は、データベースとプロンプトを差し替えることで、他科目や別ドメインの「AIチューター / アシスタント」として機能するアーキテクチャを採用しています。

別の内容に変更する際は、以下のステップと注意事項を必ず遵守してください。

1. 構造化データの入れ替え（SQLite編）
最も重要なのは、AIに確実に参照させたい「事実データ（数値、リスト、マスタデータ）」の再定義です。

🚨 注意: Pydanticモデルの厳格化 (Foolproof)

backend/app/models/ 内の型定義を、新しいデータに合わせて必ず書き換えてください。

ダメな例: value: str （何でも入ってしまう）

良い例: year: int = Field(..., ge=1868, le=2026) （歴史データなら年号の範囲を制限する）

理由: 誤った型や範囲外のデータがDBに入ると、AIがハルシネーション（嘘）をつく原因になります。

💡 ヒント: Repositoryパターンの維持

backend/app/repositories/ 内のクラス名は変更（例: PopulationRepository → HistoryRepository）しても構いませんが、「DBアクセスを隠蔽する」というインターフェースの役割は絶対に残してください。直接API内にSQLを書かないでください。

2. 非構造化データの入れ替え（Chroma DB/RAG編）
AIの「背景知識」となるテキストデータを入れ替えます。

🚨 注意: チャンクサイズの再チューニング

scripts/init_vector_db.py などのチャンキング設定（chunk_size, chunk_overlap）は、ドメインによって最適な値が異なります。

歴史（文脈が長い）: サイズを大きく（例: chunk_size=1000）

英単語や一問一答: サイズを小さく（例: chunk_size=200）

理由: 意味の区切りが不適切なチャンクが検索でヒットすると、AIの回答が不自然になります。

💡 ヒント: Embeddingモデルは共通でOK

埋め込みモデル（Gemini等）は、日本語であればドメインを問わず高性能です。変更の必要はありません。

3. エージェント層（APIとプロンプト）の変更
AIに「自分は何者か」と「どのツール（API）を使えるか」を教え直します。

🚨 注意: Tool Callingの説明文の明確化 (Fail-safe)

AIにツール（FastAPIのエンドポイント）を使わせるための description は、極めて具体的に書いてください。

ダメな例: データベースを検索します。

良い例: 日本の歴史的な出来事を年号で検索します。引数には西暦(整数)を渡してください。

理由: 説明が曖昧だと、AIが誤った引数を渡したり、不要なタイミングでAPIを叩いたりしてエラーを引き起こします。

🚨 注意: システムプロンプトの再設定

「あなたは◯◯の専門家です」という役割定義を必ず更新してください。また、「わからない場合は『わからない』と答えること」という指示（Fail-safe）は、どのドメインでも残しておくことを推奨します。
