"""
Get named arguments from terminal
    example: --task
        
"""
from project.controller import ProjectController
from project.service import ProjectService


def main():
    menu_options = [
        {"choice": 0, "label": "Get Projects"},
        {"choice": 1, "label": "Create Project"},
        {"choice": 2, "label": "Exit"}
    ]

    while True:
        print("Menu:")
        for option in menu_options:
            print(f"{option['choice']}: {option['label']}")

        choice = input("Enter your choice: ")

        selected_option = next((option for option in menu_options if option["choice"] == int(choice)), None)
        if selected_option is not None:
            if selected_option["choice"] == 0:
                get_projects()
                break
            elif selected_option["choice"] == 1:
                create()
                break
            elif selected_option["choice"] == 2:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


def get_projects():
    project_controller = ProjectController()
    response = project_controller.get_projects()
    print(response)


def create():
    project_options = ProjectService.Options()
    project_options.name = input("Enter the project name: ")
    project_options.description = input("Enter the project description: ")

    response = ProjectController().create_project(project_options)

    if response:
        print("Successfully created: {}".format(project_options.name))


if __name__ == "__main__":
    main()
