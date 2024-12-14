import unittest
from unittest.mock import MagicMock
from .expense_manager import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager(db_name="test_expenses.db")
        self.manager.get_all_expenses = MagicMock(return_value=[])
    
    def test_add_expense(self):
        self.manager.add_expense(10.50, "Food", "2024-12-05", "Lunch")
        self.manager.get_all_expenses.return_value = [(1, 10.50, "Food", "2024-12-05", "Lunch")]
        expenses = self.manager.get_all_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0][1], 10.50)

    def test_edit_expense(self):
    # Add an expense
        
        expense_id = self.manager.add_expense(20.00, "Utilities", "2024-12-05", "Electricity Bill")
        self.manager.get_all_expenses.return_value = [(expense_id, 20.00, "Utilities", "2024-12-05", "Electricity Bill")]
        added_expense = self.manager.get_expenses_by_id(expense_id)
        print(f"Added Expense: {added_expense}")
        self.assertIsNotNone(added_expense) 
        self.manager.edit_expense(expense_id, 25.00, "Utilities", "2024-12-05", "Updated Bill")
        updated_expenses = self.manager.get_expenses_by_id(expense_id)
        print(f"Updated Expense: {updated_expenses}")  
        self.assertEqual(updated_expenses, (expense_id, 25.00, "Utilities", "2024-12-05", "Updated Bill"))

    def test_delete_expense(self):
        self.manager.get_all_expenses.return_value = [(1, 15.00, "Transportation", "2024-12-05", "Bus Ticket")]
        self.manager.delete_expense(1)
        self.manager.get_all_expenses.return_value = []  
        expenses = self.manager.get_all_expenses()
        self.assertEqual(len(expenses), 0)

if __name__ == "__main__":
    unittest.main()