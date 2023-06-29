import json


class Task:
    class TaskOptions:
        def __init__(self):
            self.title = None
            self.description = None
            self.status = None

    def __init__(self, options):
        self.title = options.title or ""
        self.description = options.description or ""
        self.status = options.status or False

    def to_json(self):
        task_dict = {
            "title": self.title,
            "description": self.description,
            "status": self.status
        }
        return json.dumps(task_dict)
