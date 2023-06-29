import copy
import json
import os
import uuid
from datetime import date

from jsonschema import validate


class TaskService:
    class Options:
        def __init__(self):
            self.project_id = None
            self.title = None
            self.description = None
            self.status = False

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.project_id = None
        self.title = None
        self.description = None
        self.status = False
        self.created_at = None
        self.updated_at = None
        self.schema_file_path = os.path.join(os.path.dirname(__file__), "../task_schema.json")
        self.data_file = os.path.join(os.path.dirname(__file__), "../task_data.json")
        self.schema = self._load_schema()

    def get(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")

    def create_task(self, data: Options):
        self.title = data.title
        self.project_id = data.project_id
        self.description = data.description
        self.status = data.status
        self.created_at = date.today()

        existing_data = self.get()
        new_task = self._to_dict()
        # Clone the existing object if it exists
        new_data = copy.deepcopy(existing_data) if existing_data is not None else {}

        if "projects" in new_data:
            new_data["tasks"].append(new_task)
        else:
            new_data["tasks"] = [new_task]

        if not self._persist(new_data):
            raise Exception("Sorry data not persisted")
        return True

    def update_task(self, data: Options):
        self.title = data.title
        self.description = data.description
        self.status = data.status
        self.updated_at = date.today()

    def _persist(self, data):
        print("from persist {}".format(str(data)))
        try:
            validate(data, self.schema)
            with open(self.data_file, 'w') as file:
                json.dump(data, file)
            return True
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")
            return False

    def _to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def _load_schema(self):
        try:
            with open(self.schema_file_path) as schema_file:
                schema = json.load(schema_file)
            return schema
        except FileNotFoundError:
            print(f"Error: Schema file '{self.schema_file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Unable to parse JSON schema file '{self.schema_file_path}'.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while loading the schema file: {str(e)}")
