import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

# ExpenseManager class
class ExpenseManager:
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name
        self.categories = ["Food", "Travel", "Utilities", "Shopping", "Other"]
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

    def edit_expense(self, expense_id, amount, category, date, description=""):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE expenses
                SET amount = ?, category = ?, date = ?, description = ?
                WHERE id = ?
            """, (amount, category, date, description, expense_id))
            conn.commit()

    def delete_expense(self, expense_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            conn.commit()

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

# UIManager class
class UIManager:
    def __init__(self, root):
        self.root = root
        self.manager = ExpenseManager()
        self.root.title("Expense Tracker")
        self.bg_color = "#f7f7f7"
        self.header_color = "#4caf50"
        self.button_color = "#4caf50"
        self.button_text_color = "white"
        self.text_color = "#333"
        self.root.configure(bg=self.bg_color)
        self.create_main_window()

    def create_main_window(self):
        header = tk.Label(self.root, text="Expense Tracker", bg=self.header_color, fg="white", font=("Arial", 18, "bold"))
        header.pack(fill=tk.X, pady=10)

        table_frame = tk.Frame(self.root, bg=self.bg_color)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Amount", "Category", "Date", "Description"), show="headings", height=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Description", text="Description")
        self.tree.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(fill=tk.X, pady=10)

        add_button = tk.Button(button_frame, text="Add Expense", bg=self.button_color, fg=self.button_text_color,
                               command=self.create_add_expense_window, font=("Arial", 12, "bold"))
        add_button.pack(side=tk.LEFT, padx=10, pady=5)

        edit_button = tk.Button(button_frame, text="Edit Expense", bg=self.button_color, fg=self.button_text_color,
                                command=self.create_edit_expense_window, font=("Arial", 12, "bold"))
        edit_button.pack(side=tk.LEFT, padx=10, pady=5)

        delete_button = tk.Button(button_frame, text="Delete Expense", bg=self.button_color, fg=self.button_text_color,
                                  command=self.delete_selected_expense, font=("Arial", 12, "bold"))
        delete_button.pack(side=tk.LEFT, padx=10, pady=5)

        summary_button = tk.Button(button_frame, text="View Summary", bg=self.button_color, fg=self.button_text_color,
                                   command=self.display_summary, font=("Arial", 12, "bold"))
        summary_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.update_expense_table()

    def create_add_expense_window(self):
        self._create_expense_window("Add Expense", self.manager.add_expense)

    def create_edit_expense_window(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No expense selected!")
            return

        expense_id = int(self.tree.item(selected_item, "values")[0])
        current_data = self.tree.item(selected_item, "values")
        self._create_expense_window("Edit Expense", self.manager.edit_expense, expense_id, current_data)

    def _create_expense_window(self, title, save_action, expense_id=None, current_data=None):
        expense_window = tk.Toplevel(self.root)
        expense_window.title(title)
        expense_window.configure(bg=self.bg_color)

        tk.Label(expense_window, text="Amount:", bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
        amount_entry = tk.Entry(expense_window, font=("Arial", 12))
        amount_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(expense_window, text="Category:", bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        category_combobox = ttk.Combobox(expense_window, values=self.manager.categories, state="readonly", font=("Arial", 12))
        category_combobox.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(expense_window, text="Date (YYYY-MM-DD):", bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
        date_entry = tk.Entry(expense_window, font=("Arial", 12))
        date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(expense_window, text="Description:", bg=self.bg_color, fg=self.text_color, font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
        description_entry = tk.Entry(expense_window, font=("Arial", 12))
        description_entry.grid(row=3, column=1, padx=5, pady=5)

        if current_data:
            amount_entry.insert(0, current_data[1])
            category_combobox.set(current_data[2])
            date_entry.insert(0, current_data[3])
            description_entry.insert(0, current_data[4])

        def save():
            try:
                amount = float(amount_entry.get())
                category = category_combobox.get()
                date = datetime.strptime(date_entry.get(), "%Y-%m-%d").date()
                description = description_entry.get()
                if category not in self.manager.categories:
                    raise ValueError("Invalid category!")

                if expense_id:
                    save_action(expense_id, amount, category, str(date), description)
                else:
                    save_action(amount, category, str(date), description)

                self.update_expense_table()
                expense_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        save_button = tk.Button(expense_window, text="Save", bg=self.button_color, fg=self.button_text_color, command=save, font=("Arial", 12, "bold"))
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def delete_selected_expense(self):
        selected_item = self.tree.selection()
        if selected_item:
            expense_id = int(self.tree.item(selected_item, "values")[0])
            self.manager.delete_expense(expense_id)
            self.update_expense_table()
        else:
            messagebox.showwarning("Warning", "No expense selected!")

    def display_summary(self):
        summary = self.manager.get_expense_summary()
        summary_text = "\n".join([f"{category}: ${amount:.2f}" for category, amount in summary])
        messagebox.showinfo("Expense Summary", summary_text if summary_text else "No expenses recorded.")

    def update_expense_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for expense in self.manager.get_all_expenses():
            self.tree.insert("", "end", values=expense)

if __name__ == "__main__":
    root = tk.Tk()
    app = UIManager(root)
    root.mainloop()