import json
from datetime import datetime


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []   

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def next_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1
    
    def add_task(self, description):
        now = datetime.now().isoformat()
        task = {"id": self.next_id(), "description": description, "status": "todo", "createdAt":now, "updatedAt":now}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task['id']})")
    