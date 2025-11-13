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
    
    def task_finder(self, id):
        for task in self.tasks:
            if task["id"] == id:
                return task
        return {}
    
    def add_task(self, description):
        now = datetime.now().isoformat()
        task = {"id": self.next_id(), "description": description, "status": "todo", "createdAt":now, "updatedAt":now}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task['id']})")
    
    def update_task(self, id, new_description):
        task = self.task_finder(id)
        if task == {}:
            print(f"Task with id {id} not found.")
            return
        task["description"] = new_description
        task["updatedAt"] = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {id} updated successfully.")

    def delete_task(self, id):
        task = self.task_finder(id)
        if task == {}:
            print(f"Task with id {id} not found.")
            return
        self.tasks.remove(task)
        self.save_tasks()
        print(f"Task {id} deleted successfully.")

    def change_status_task(self, id, new_status):
        task = self.task_finder(id)
        if task == {}:
            print(f"Task with id {id} not found.")
            return
        if(task["status"] == new_status):
            print(f"Task {id} is already marked as {new_status}.")
            return
        task["status"] = new_status
        task["updatedAt"] = datetime.now().isoformat()
        self.save_tasks()
        print(f"Task {id} has been marked as {new_status}.")

    def list_task(self, status):
        if status:
            tasks_to_show = [task for task in self.tasks if task["status"] == status]
        else:
            tasks_to_show = self.tasks

        if not tasks_to_show:
            print("No tasks found.")
            return
        
        for task in tasks_to_show:
            print(f"[{task['id']}] {task['description']} - {task['status']}")