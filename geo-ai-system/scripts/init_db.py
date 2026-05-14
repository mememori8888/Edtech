# scripts/init_db.py
import pandas as pd
import sqlite3
from backend.app.models.population import PopulationData

def setup_database():
    csv_path = "data/census_population.csv"
    db_path = "geography_edu.db"
    
    # データの読み込み
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: {csv_path} が見つかりません。")
        return

    # バリデーション & インポート
    with sqlite3.connect(db_path) as conn:
        valid_rows = []
        for _, row in df.iterrows():
            try:
                # 1行ずつチェック (Foolproof)
                data = PopulationData(**row.to_dict())
                valid_rows.append(data.dict())
            except Exception as e:
                print(f"スキップされた行: {row['country_name']} - {e}")
        
        # SQLへ書き出し
        pd.DataFrame(valid_rows).to_sql("populations", conn, if_exists="replace", index=False)
        print(f"完了: {len(valid_rows)} 件のデータを保存しました。")

if __name__ == "__main__":
    setup_database()