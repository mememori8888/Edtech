# tests/test_ai_quality.py
import pytest
import time
# 👇 これらが抜けていました！失礼いたしました。
from agent.question_generator import QuestionGeneratorAgent

def test_ai_question_format():
    """AIが生成した問題が、正常なデータをもとに正しい形式で作られているか"""
    agent = QuestionGeneratorAgent()
    
    # 1. 実際にAIを動かす
    result = agent.generate_integrated_question("Japan", "人口転換")
    
    # --- 🚨 修正：Noneチェックを最優先にする ---
    assert result is not None, "❌ AIからの返却値が完全に空（None）です"
    
    # --- 2. インプットデータの健全性チェック ---
    assert "データ取得エラー" not in result, "❌ システム内部でデータ取得に失敗しています！"
    assert "HTTP" not in result, "❌ 通信エラーが発生しています！"
    
    # --- 3. 既存のフォーマットチェック ---
    assert "【問題】" in result, "❌ 【問題】タグが含まれていません"
    assert "【正解】" in result, "❌ 【正解】タグが含まれていません"
    
    for i in range(1, 5):
        assert f"{i}." in result, f"選択肢 {i}. が見つかりません"
        
    print("\n✅ AI品質テスト（形式・データ健全性）に完全合格しました！")
    print("LangSmithへのログ送信を待機中...")
    time.sleep(3)