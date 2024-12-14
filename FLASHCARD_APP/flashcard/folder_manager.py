from .flashcard import FlashCard

class FolderManager:
    def __init__(self):
        self.folders = {}

    def add_folder(self, folder_name):
        if folder_name not in self.folders:
            self.folders[folder_name] = []

    def delete_folder(self, folder_name):
        if folder_name in self.folders:
            del self.folders[folder_name]

    def add_flashcard_to_folder(self, folder_name, question, answer):
        if folder_name in self.folders:
            self.folders[folder_name].append(FlashCard(question, answer))

    def get_folders(self):
        return list(self.folders.keys())

    def get_flashcards_from_folder(self, folder_name):
        return self.folders.get(folder_name, [])