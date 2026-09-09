import sqlite3
from pathlib import Path
from typing import List, Tuple

DB_PATH = Path(__file__).parent / "cafe.db"


def init_db() -> None:
    """Создаёт таблицу drinks, если она ещё не существует."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS drinks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL
            )
            """
        )
        conn.commit()


def add_drink(name: str, price: int) -> None:
    """Добавляет новый напиток в базу данных."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO drinks (name, price) VALUES (?, ?)",
            (name, price),
        )
        conn.commit()


def get_all_drinks() -> List[Tuple[str, int]]:
    """Возвращает список всех напитков в виде (название, цена)."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT name, price FROM drinks ORDER BY id")
        return cursor.fetchall()