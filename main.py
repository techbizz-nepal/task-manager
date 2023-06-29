from json_data_source import JsonDataSource
from project import Project
from task import Task

""" 
Get named arguments from terminal
    example: --task
        
"""


def main():
    json_data_source_options = JsonDataSource.JsonDataSourceOptions()
    task_options = Task.TaskOptions()
    project_options = Project.ProjectOptions()

    json_data_source_options.schema_file_path = "schema.json"
    json_data_source_options.file_to_read = "data.json"
    json_data_source_options.file_to_write = "data.json"

    task_options.title = "Task 1"
    task_options.description = None
    task_options.status = False

    task_one = Task(task_options)

    project_options.name = "POC"
    project_options.tasks = [task_one]

    project_one = Project(project_options)

    json_data_source = JsonDataSource(json_data_source_options)
    json_to_persist = {
        "projects": [project_one.to_json()]
    }
    # json_data_source.persist(json_to_persist)
    print(project_one.to_json())


if __name__ == "__main__":
    main()
