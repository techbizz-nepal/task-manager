from project.service import ProjectService


class ProjectController:
    def __init__(self):
        self.project_service = ProjectService()

    def get_projects(self):
        return self.project_service.get()

    def create_project(self, data: ProjectService.Options):
        try:
            return self.project_service.create_project(data)
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")

    def edit_project(self):
        pass

    def delete_project(self):
        pass
