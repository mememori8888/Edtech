# tests/test_ai_quality.py
import pytest
from agent.question_generator import QuestionGeneratorAgent
import time

def test_ai_question_format():
    """AIが生成した問題のフォーマットが正しいかチェックする"""
    # エージェントの初期化（API_BASE_URLは本番URLがデフォルトで使われます）
    agent = QuestionGeneratorAgent()
    
    # 実際にAIに問題を1件作らせる
    result = agent.generate_integrated_question("Japan", "人口転換")
    
    # 検証（これが満たされないとテストが落ちる）
    assert result is not None, "AIの回答が空です"
    assert "【問題】" in result, "【問題】タグが含まれていません"
    assert "【正解】" in result, "【正解】タグが含まれていません"
    
    # 選択肢がちゃんとあるか
    for i in range(1, 5):
        assert f"{i}." in result, f"選択肢 {i}. が見つかりません"
        
    print("\n✅ AI品質テスト（形式）に合格しました！")
    # 👇 ログを送信し切るために、最後に3秒だけプログラムを意図的に歩かせる
    print("LangSmithへのログ送信を待機中...")
    time.sleep(3)
