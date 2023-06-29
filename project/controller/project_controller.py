from project.service import ProjectService


class ProjectController:
    def __init__(self):
        self.project_service = ProjectService()

    def get_projects(self):
        return self.project_service.get_projects()

    def find_by_id(self, project_id: str):
        return self.project_service.find_by_id(project_id)

    def get_by_id(self, project_id: str):
        return self.project_service.get_by_id(project_id)

    def create_project(self, data: ProjectService.Options):
        try:
            return self.project_service.create_project(data)
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")

    def edit_project(self):
        pass

    def delete_project(self):
        pass
