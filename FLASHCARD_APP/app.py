import tkinter as tk
from flashcard.ui import FlashCardApp

def main():
    root = tk.Tk()
    app = FlashCardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()