import sqlite3
from datetime import datetime
from .base_classes import BaseManager

class ExpenseManager(BaseManager):
    def __init__(self, db_name="expenses.db"):
        super().__init__(db_name)
        self.expenses = []
        self.categories = ["Food", "Transportation", "Utilities", "Shopping", "Other"]
        self._initialize_database()
        
            
    def _initialize_database(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT
                )
            """)
            conn.commit()

    def add_expense(self, amount, category, date, description=""):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses (amount, category, date, description)
                VALUES (?, ?, ?, ?)
            """, (amount, category, date, description))
            conn.commit()
            return cursor.lastrowid    

    def edit_expense(self, expense_id, new_amount, new_category, new_date, new_description=""):
        for i, expense in enumerate(self.expenses):
            if expense[0] == expense_id:
                self.expenses[i] = (expense_id, new_amount, new_category, new_date, new_description)
                return
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE expenses
                SET amount = ?, category = ?, date = ?, description = ?
                WHERE id = ?
            """, (new_amount, new_category, new_date, new_description, expense_id))
            conn.commit()

    def delete_expense(self, expense_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()
            
    def get_expenses_by_id(self, expense_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
            result = cursor.fetchone()
            return result

    def get_all_expenses(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            return cursor.fetchall()

    def get_expense_summary(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
            return cursor.fetchall()
        
    def clear_expenses(self):
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses")
            conn.commit()
            print("All expenses have been cleared")
        except sqlite3.Error as e:
            print(f"An error occurredwhile clearing expense: {e}")
            
        finally:
            if conn:
                conn.close()