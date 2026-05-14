# ui/app.py
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
import sys # ← これを追加

# --- ここから追加 (パスの解決) ---
# 現在のファイル(app.py)があるディレクトリの、1つ上のディレクトリ(geo-ai-system)をパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
# --- ここまで追加 ---

# ページ設定
st.set_page_config(page_title="GeoAI Tutor", layout="wide")

# 設定 (Fail-safe: FastAPIのURL)
API_BASE_URL = "https://edtech-wsqi.onrender.com/api/v1"

st.title("🌏 GeoAI 学習支援システム")
st.markdown("---")

# サイドバー: 設定
st.sidebar.header("学習設定")

# 修正ポイント1: "USA" を "United States" に修正し、主要な国を追加
# ※本来はDBから動的に取得するのがベストですが、まずはリストを拡充しています
country_list = [
    "Japan", 
    "Nigeria", 
    "United States", 
    "China", 
    "India", 
    "Brazil", 
    "Indonesia", 
    "Pakistan", 
    "Bangladesh"
]
target_country = st.sidebar.selectbox("国を選択", country_list)

target_topic = st.sidebar.text_input("学習トピック", value="人口転換")

# メインレイアウト: 2カラム
col_left, col_right = st.columns([1, 1])

# --- 左カラム: 統計データの可視化 (SQLite) ---
with col_left:
    st.subheader(f"📊 {target_country} の人口統計データ")
    
    try:
        res = requests.get(f"{API_BASE_URL}/population/{target_country}")
        if res.status_code == 200:
            data = res.json()["data"]
            df = pd.DataFrame(data)
            
            # グラフの描画 (Plotly)
            fig = px.line(df, x="year", y="midyear_population", 
                         title=f"{target_country} の人口推移 (1950-2050)",
                         labels={"midyear_population": "人口", "year": "年"})
            st.plotly_chart(fig, use_container_width=True)
            
            st.dataframe(df)
        else:
            # 修正ポイント: エラー時に理由を表示
            st.warning(f"'{target_country}' のデータがデータベースに見つかりませんでした。")
    except Exception as e:
        st.error(f"API接続エラー: {e}")

# --- 右カラム: AIエージェント (RAG + 問題生成) ---
with col_right:
    st.subheader("🤖 AIチューター：類題生成")
    
    if st.button(f"{target_topic} に関する問題を生成"):
        with st.spinner("AIがデータと背景知識を分析して問題を作成中..."):
            try:
                # エージェントロジックを呼び出す
                from agent.question_generator import QuestionGeneratorAgent
                
                agent = QuestionGeneratorAgent()
                question_text = agent.generate_integrated_question(target_country, target_topic)
                
                st.markdown("### AIが作成したオリジナル問題")
                
                # 修正ポイント2: 「【正解】」でテキストを分割し、答えを隠すギミック
                if "【正解】" in question_text:
                    # テキストを「【正解】」というキーワードで分割
                    q_part, a_part = question_text.split("【正解】", 1)
                    
                    # 問題部分のみを表示
                    st.info(q_part)
                    
                    # 正解と解説はアコーディオン（折りたたみ）の中に隠す
                    with st.expander("👉 答えと解説を確認する"):
                        st.success(f"**【正解】** {a_part}")
                else:
                    # 万が一AIがフォーマットに従わなかった場合のFail-safe
                    st.info(question_text)
                
            except Exception as e:
                st.error(f"問題生成エラー: {e}")

    # RAG検索の単体テスト用
    with st.expander("参照されている背景知識を確認 (RAG)"):
        search_res = requests.post(f"{API_BASE_URL}/knowledge/search", json={"query": target_topic})
        if search_res.status_code == 200:
            results = search_res.json()["results"]
            if not results:
                st.write("該当する知識がChroma DBに見つかりませんでした。")
            else:
                for i, txt in enumerate(results):
                    st.write(f"【知識 {i+1}】")
                    st.caption(txt)