# manager.py

import json
import os
from task import Task

DATA_FILE = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title, priority="medium"):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: {task.title}")

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. [{task.status.upper
