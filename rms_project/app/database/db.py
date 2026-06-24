import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Database:
    def __init__(self, file):
        self.file = os.path.join(BASE_DIR, file)

        os.makedirs(os.path.dirname(self.file), exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)