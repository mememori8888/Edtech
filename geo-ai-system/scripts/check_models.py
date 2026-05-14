# scripts/check_models.py
import os
import google.generativeai as genai

# Codespaces環境とローカル環境の両方に対応 (Fail-safe)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def check_available_models():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("エラー: GOOGLE_API_KEY が見つかりません。")
        return

    genai.configure(api_key=api_key)
    print("あなたのAPIキーで利用可能な「埋め込み(Embedding)モデル」を検索しています...")
    
    found = False
    try:
        # APIに利用可能な全モデルを問い合わせる
        for m in genai.list_models():
            if "embedContent" in m.supported_generation_methods:
                print(f"利用可能: {m.name}")
                found = True
                
        if not found:
            print("利用可能な埋め込みモデルが一つも見つかりませんでした。")
    except Exception as e:
        print(f"API通信エラー: {e}")

if __name__ == "__main__":
    check_available_models()