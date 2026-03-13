import json
from datetime import datetime
from pathlib import Path

# filepath: c:\Users\PC\Downloads\task_manager.py


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, title, description=""):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        self.save_tasks()
    
    def list_tasks(self, completed=None):
        if completed is None:
            return self.tasks
        return [t for t in self.tasks if t["completed"] == completed]

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Learn Python", "Complete the basics course")
    manager.add_task("Build a project")
    print(manager.list_tasks())