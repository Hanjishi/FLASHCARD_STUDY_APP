class Expense:
    def __init__(self, exepense_id, amount, category, date, description=""):
        self.exepense_id = exepense_id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        
    def __to_tuple(self):
        return (self.exepense_id, self.amount, self.category, self.date, self.description)