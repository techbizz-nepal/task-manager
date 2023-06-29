import copy
import json
import os
import uuid
from datetime import date

from jsonschema import validate


class ProjectService:
    class Options:
        def __init__(self):
            self.name = ""
            self.description = ""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.description = ""
        self.name = ""
        self.created_at = ""
        self.updated_at = ""
        self.schema_file_path = os.path.join(os.path.dirname(__file__), "../project_schema.json")
        self.data_file = os.path.join(os.path.dirname(__file__), "../project_data.json")
        self.schema = self._load_schema()

    def get_projects(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")

    def find_by_id(self, project_id: str):
        projects = self.get_projects().get("projects", [])
        return next((project for project in projects if project.get('id') == project_id), None)

    def get_by_id(self, project_id: str):
        projects = self.get_projects().get("projects", [])
        return [project for project in projects if project.get('id') == project_id]

    def create_project(self, data: Options):
        self.name = data.name
        self.description = data.description
        self.created_at = str(date.today())
        existing_data = self.get_projects()
        new_project = self._to_dict()
        # Clone the existing object if it exists
        new_data = copy.deepcopy(existing_data) if existing_data is not None else {}

        if "projects" in new_data:
            new_data["projects"].append(new_project)
        else:
            new_data["projects"] = [new_project]
        if not self._persist(new_data):
            raise Exception("Sorry data not persisted")
        return True

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
            "name": self.name,
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
