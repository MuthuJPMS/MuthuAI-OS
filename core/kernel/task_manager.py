from datetime import datetime


class TaskManager:

    def __init__(self):
        self.tasks = []


    def create_task(self, task):

        new_task = {
            "id": len(self.tasks)+1,
            "task": task,
            "status": "created",
            "created_at": datetime.now().isoformat()
        }

        self.tasks.append(new_task)

        return new_task


    def update_status(self, task_id, status):

        for task in self.tasks:

            if task["id"] == task_id:
                task["status"] = status
                return task


    def get_tasks(self):

        return self.tasks



task_manager = TaskManager()