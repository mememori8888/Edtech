# backend/app/repositories/population_repository.py
import sqlite3
from typing import List

class PopulationRepository:
    """Repositoryパターン: SQLiteへのアクセスを隠蔽"""
    
    def __init__(self, db_path: str = "geography_edu.db"):
        self.db_path = db_path

    def get_by_country(self, country_name: str) -> List[dict]:
        """Fail-safe: DB接続エラー時は空のリストを返しシステムダウンを防ぐ"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                # 特定の国の全年代のデータを取得
                cursor.execute(
                    "SELECT * FROM populations WHERE country_name = ? ORDER BY year",
                    (country_name,)
                )
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Database Error: {e}")
            return []