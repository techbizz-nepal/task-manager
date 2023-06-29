from task.service import TaskService


class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    def get_tasks(self):
        return self.task_service.get()

    def create_task(self, data: TaskService.Options):
        try:
            return self.task_service.create_task(data)
        except Exception as e:
            print(f"Error: An unexpected error occurred while persisting the JSON data: {str(e)}")

    def edit_task(self):
        pass

    def delete_task(self):
        pass
