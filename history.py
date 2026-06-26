import json

class History:
    def __init__(self):
        self.entries = []

    def add(self, entry: str):
        self.entries.append(entry)

    def show(self):
        return self.entries

    def save(self, filename: str):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.entries, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"Ошибка сохранения истории: {e}")

    def load(self, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.entries = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.entries = []
            print(f"История не загружена (файл отсутствует или повреждён). Будет создана новая.")