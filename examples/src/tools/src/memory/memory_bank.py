import json
import os

class MemoryBank:
    def __init__(self, path="memory/winning_templates.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({"wins": []}, f)

    def load(self):
        with open(self.path) as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def store_win(self, variant):
        data = self.load()
        data["wins"].append(variant)
        self.save(data)
