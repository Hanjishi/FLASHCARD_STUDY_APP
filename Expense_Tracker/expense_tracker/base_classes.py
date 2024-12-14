class BaseManager(object):
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name

class BaseUI(object):
    def __init__(self, root):
        self.root = root
        self.bg_color = "#f7f7f7"
        self.header_color = "#4caf50"
        self.button_color = "#4caf50"
        self.button_text_color = "white"
        self.text_color = "#333"
        self.root.configure(bg=self.bg_color)