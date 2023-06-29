import json
from typing import List, Optional
from task import Task


class Project:
    class ProjectOptions:
        # def __init__(self, name: str, tasks: Optional[List[Task]] = None, description: Optional[str] = None):
        #     self.name = name
        #     self.tasks = tasks if tasks is not None else []
        #     self.description = description

        def __init__(self):
            self.name = None
            self.tasks = None
            self.description = None

    def __init__(self, options):
        self.name = options.name or ""
        self.tasks = options.tasks or []
        self.description = options.description or ""

    def to_json(self):
        project_dict = {
            "name": self.name,
            "tasks": [task.to_json() for task in self.tasks],
            "description": self.description
        }
        return json.dumps(project_dict)
