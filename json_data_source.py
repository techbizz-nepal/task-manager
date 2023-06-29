import json
from jsonschema import validate


class JsonDataSource:
    class JsonDataSourceOptions:
        def __init__(self):
            self.file_to_read = None
            self.file_to_write = None
            self.schema_file_path = None

    def __init__(self, options):
        self.schema_file_path = options.schema_file_path
        self.file_to_read = options.file_to_read
        self.file_to_write = options.file_to_write
        self.schema = self._load_schema()

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

    def read_json_file(self):
        try:
            with open(self.file_to_read) as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: File '{self.file_to_read}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Unable to parse JSON data in file '{self.file_to_read}'.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while reading the file: {str(e)}")

    def persist(self, data):
        try:
            validate(data, self.schema)
            with open(self.file_to_write, 'w') as file:
                json.dump(data, file)
            print(f"Successfully persisted JSON data to file '{self.file_to_read}'.")
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")
