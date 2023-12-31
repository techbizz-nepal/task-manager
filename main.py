"""
Get named arguments from terminal
    example: --task
        
"""

from project.controller import ProjectController
from project.service import ProjectService
from task.controller import TaskController


def main():
    menu_options = [
        {"choice": 1, "label": "Get Projects"},
        {"choice": 2, "label": "Create Project"},
        {"choice": 3, "label": "Get Tasks"},
        {"choice": 4, "label": "Create Task"},
        {"choice": 0, "label": "Exit"}
    ]

    while True:
        print("Menu:")
        for option in menu_options:
            print(f"{option['choice']}: {option['label']}")

        choice = input("Enter your choice: ")

        selected_option = next((option for option in menu_options if option["choice"] == int(choice)), None)
        if selected_option is not None:
            if selected_option["choice"] == 1:
                get_projects()
                break
            elif selected_option["choice"] == 2:
                create_project()
                break
            elif selected_option["choice"] == 3:
                get_tasks()
                break
            elif selected_option["choice"] == 4:
                create_task()
                break
            elif selected_option["choice"] == 0:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


def get_projects():
    project_controller = ProjectController()
    response = project_controller.get_projects()
    print(response)


def create_project():
    project_options = ProjectService.Options()
    project_options.name = input("Enter the project name: ")
    project_options.description = input("Enter the project description: ")

    response = ProjectController().create_project(project_options)

    if response:
        print("Successfully created: {}".format(project_options.name))


def get_tasks():
    task_controller = TaskController()
    response = task_controller.get_tasks()
    print(response)


def create_task():
    project_controller = ProjectController()
    project_id = "7f64b296-c1c6-474b-99de-f48b374056cc"
    dd = project_controller.get_projects()

    print("project by id {}".format(project_id))
    print(dd)


if __name__ == "__main__":
    main()
