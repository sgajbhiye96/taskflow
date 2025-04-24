# task.py

import datetime
import uuid

class Task:
    def __init__(self, title, priority="medium", status="pending"):
        self.id = str(uuid.uuid4())  # Unique ID for each task
        self.title = title
        self.priority = priority
        self.status = status
        self.created_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["priority"], data["status"])
        task.id = data["id"]
        task.created_at = data["created_at"]
        return task
