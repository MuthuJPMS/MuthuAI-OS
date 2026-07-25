from datetime import datetime
import uuid

from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor

from core.events.event_bus import event_bus



class TaskManager:


    def __init__(self):

        self.tasks = {}

        health_monitor.register_component(
            "Task Manager"
        )



    def create_task(
        self,
        name,
        priority="normal",
        metadata=None
    ):


        task_id = str(uuid.uuid4())


        task = {

            "id": task_id,

            "name": name,

            "priority": priority,

            "status": "pending",

            "metadata": metadata or {},

            "created_at":
                datetime.now().isoformat()

        }


        self.tasks[task_id] = task


        event_bus.publish(

            "task_created",

            "Task Manager",

            task

        )


        logger.info(
            f"Task created: {name}"
        )


        return task



    def start_task(self, task_id):


        if task_id not in self.tasks:

            return None


        self.tasks[task_id]["status"] = "running"


        event_bus.publish(

            "task_started",

            "Task Manager",

            self.tasks[task_id]

        )


        return self.tasks[task_id]



    def complete_task(
        self,
        task_id,
        result=None
    ):


        if task_id not in self.tasks:

            return None


        self.tasks[task_id]["status"] = "completed"

        self.tasks[task_id]["result"] = result

        self.tasks[task_id]["completed_at"] = (
            datetime.now().isoformat()
        )


        event_bus.publish(

            "task_completed",

            "Task Manager",

            self.tasks[task_id]

        )


        return self.tasks[task_id]



    def fail_task(
        self,
        task_id,
        error
    ):


        if task_id not in self.tasks:

            return None


        self.tasks[task_id]["status"] = "failed"

        self.tasks[task_id]["error"] = error


        event_bus.publish(

            "task_failed",

            "Task Manager",

            self.tasks[task_id]

        )


        return self.tasks[task_id]



    def get_all_tasks(self):

        return list(
            self.tasks.values()
        )



    def get_task(self, task_id):

        return self.tasks.get(task_id)



task_manager = TaskManager()