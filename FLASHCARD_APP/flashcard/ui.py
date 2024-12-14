import tkinter as tk
from tkinter import messagebox, colorchooser
import random
from .folder_manager import FolderManager

class FlashCardApp:
    def __init__(self, root):
        self.manager = FolderManager()
        self.current_folder = None
        self.root = root
        self.root.title("Flash Card Study App")

        # Default Theme
        self.bg_color = "white"
        self.fg_color = "black"
        self.button_bg_color = "lightgrey"

        self.build_interface()

    def build_interface(self):
        # Title of the Application
        title_frame = tk.Frame(self.root, bg=self.bg_color)
        title_frame.pack(fill=tk.X, pady=5)

        title_label = tk.Label(
            title_frame,
            text="Flash Card Study App",
            font=("Arial", 24, "bold"),
            fg="blue",
            bg=self.bg_color,
        )
        title_label.pack(side=tk.TOP, pady=10)

        # Change Theme Button
        theme_button = tk.Button(
            title_frame,
            text="Change Theme",
            command=self.change_theme,
            bg=self.button_bg_color,
            fg=self.fg_color,
        )
        theme_button.pack(side=tk.TOP, pady=10)

        # Main Menu Frame
        menu_frame = tk.Frame(self.root, bg=self.bg_color)
        menu_frame.pack(pady=10)

        tk.Button(
            menu_frame,
            text="Add Folder",
            command=self.add_folder_dialog,
            width=15,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            menu_frame,
            text="Delete Folder",
            command=self.delete_folder_dialog,
            width=15,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            menu_frame,
            text="Add Flashcard",
            command=self.add_flashcard_dialog,
            width=15,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            menu_frame,
            text="Start Study Session",
            command=self.start_study_session,
            width=15,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).grid(row=1, column=1, padx=5, pady=5)

        # Folder and Flashcard Sections in One Frame
        sections_frame = tk.Frame(self.root, bg=self.bg_color)
        sections_frame.pack(pady=10)

        # Folder Section
        folder_frame = tk.Frame(sections_frame, bg=self.bg_color)
        folder_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(
            folder_frame, text="Folders", font=("Arial", 12, "bold"), bg=self.bg_color, fg=self.fg_color
        ).pack()
        self.folder_list = tk.Listbox(folder_frame, width=30, height=15)
        self.folder_list.pack(pady=5)
        self.folder_list.bind("<<ListboxSelect>>", self.select_folder)

        # Flashcard Section
        flashcard_frame = tk.Frame(sections_frame, bg=self.bg_color)
        flashcard_frame.pack(side=tk.LEFT, padx=10)

        tk.Label(
            flashcard_frame,
            text="Flashcards",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        ).pack()
        self.flashcard_list = tk.Listbox(flashcard_frame, width=50, height=15)
        self.flashcard_list.pack(pady=5)

        self.update_folder_list()

    def update_folder_list(self):
        self.folder_list.delete(0, tk.END)
        for folder in self.manager.get_folders():
            self.folder_list.insert(tk.END, folder)
        self.update_flashcard_list()

    def update_flashcard_list(self):
        self.flashcard_list.delete(0, tk.END)
        if self.current_folder:
            for card in self.manager.get_flashcards_from_folder(self.current_folder):
                self.flashcard_list.insert(tk.END, card.question)

    def select_folder(self, event):
        selected = self.folder_list.curselection()
        if selected:
            self.current_folder = self.folder_list.get(selected[0])
            self.update_flashcard_list()

    def add_folder_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Folder")

        tk.Label(dialog, text="Folder Name:").pack(pady=5)
        folder_entry = tk.Entry(dialog, width=40)
        folder_entry.pack(pady=5)

        def save_folder():
            folder_name = folder_entry.get().strip()
            if folder_name:
                self.manager.add_folder(folder_name)
                self.update_folder_list()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Folder name cannot be empty!")

        tk.Button(dialog, text="Save", command=save_folder).pack(pady=10)

    def delete_folder_dialog(self):
        selected = self.folder_list.curselection()
        if selected:
            folder_name = self.folder_list.get(selected[0])
            self.manager.delete_folder(folder_name)
            self.update_folder_list()
        else:
            messagebox.showerror("Error", "No folder selected!")

    def add_flashcard_dialog(self):
        if not self.current_folder:
            messagebox.showerror("Error", "Please select a folder first!")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title(f"Add Flashcard to Folder: {self.current_folder}")

        tk.Label(dialog, text="Question:").pack(pady=5)
        question_entry = tk.Entry(dialog, width=40)
        question_entry.pack(pady=5)

        tk.Label(dialog, text="Answer:").pack(pady=5)
        answer_entry = tk.Entry(dialog, width=40)
        answer_entry.pack(pady=5)

        def save_flashcard():
            question = question_entry.get().strip()
            answer = answer_entry.get().strip()
            if question and answer:
                self.manager.add_flashcard_to_folder(self.current_folder, question, answer)
                self.update_flashcard_list()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Both question and answer must be provided!")

        tk.Button(dialog, text="Save", command=save_flashcard).pack(pady=10)

    def start_study_session(self):
        if not self.current_folder:
            messagebox.showerror("Error", "Please select a folder to study!")
            return

        flashcards = self.manager.get_flashcards_from_folder(self.current_folder)

        if not flashcards:
            messagebox.showerror("Error", f"No flashcards in folder '{self.current_folder}'!")
            return

        random.shuffle(flashcards)  # Shuffle flashcards for random order
        study_window = tk.Toplevel(self.root)
        study_window.title(f"Study Session: {self.current_folder}")
        study_window.config(bg=self.bg_color)

        current_index = [0]
        total_cards = len(flashcards)
        score = [0]

        def show_question():
            if current_index[0] < total_cards:
                question_label.config(
                    text=f"Q: {flashcards[current_index[0]].question}",
                    bg=self.bg_color,
                    fg=self.fg_color,
                )
                answer_entry.delete(0, tk.END)
                feedback_label.config(text="")
            else:
                end_session()

        def check_answer():
            user_answer = answer_entry.get().strip()
            correct_answer = flashcards[current_index[0]].answer
            if user_answer.lower() == correct_answer.lower():
                feedback_label.config(text="✅ Correct!", fg="green")
                score[0] += 1
            else:
                feedback_label.config(text=f"❌ Wrong! Correct: {correct_answer}", fg="red")

        def next_card():
            current_index[0] += 1
            show_question()

        def end_session():
            mastery_percentage = (score[0] / total_cards) * 100
            messagebox.showinfo(
                "Study Session Complete",
                f"Score: {score[0]}/{total_cards}\nMastery: {mastery_percentage:.2f}%"
            )
            study_window.destroy()

        question_label = tk.Label(study_window, text="", font=("Arial", 16), wraplength=300, bg=self.bg_color)
        question_label.pack(pady=10)

        answer_entry = tk.Entry(study_window, width=30)
        answer_entry.pack(pady=5)

        feedback_label = tk.Label(study_window, text="", font=("Arial", 14), bg=self.bg_color)
        feedback_label.pack(pady=10)

        tk.Button(
            study_window,
            text="Check Answer",
            command=check_answer,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).pack(pady=5)

        tk.Button(
            study_window,
            text="Next",
            command=next_card,
            bg=self.button_bg_color,
            fg=self.fg_color,
        ).pack(pady=5)

        show_question()

    def change_theme(self):
        color = colorchooser.askcolor(title="Pick a Color")[1]
        if color:
            self.bg_color = color
            self.update_theme()

    def update_theme(self):
        self.root.config(bg=self.bg_color)
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.config(bg=self.bg_color)
            elif isinstance(widget, tk.Button):
                widget.config(bg=self.button_bg_color, fg=self.fg_color)
            elif isinstance(widget, tk.Label):
                widget.config(bg=self.bg_color, fg=self.fg_color)