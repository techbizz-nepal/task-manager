import json
import random


class Task:
    class TaskOptions:
        def __init__(self):
            self.title = None
            self.description = None
            self.status = None

    def __init__(self, options):
        self.id = random.Random
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


def main():
    print("hello from task")


if __name__ == "__main__":
    main()
