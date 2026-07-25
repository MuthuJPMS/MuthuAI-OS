from datetime import datetime
import uuid

from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor
from core.infrastructure.dependency_container import container

from core.events.event_bus import event_bus



class MuthuAIKernel:


    def __init__(self):

        self.tasks = {}

        health_monitor.register_component(
            "Kernel"
        )

        container.register(
            "kernel",
            self
        )

        logger.info(
            "MuthuAI Kernel initialized"
        )



    def create_task(self, goal):


        task_id = str(uuid.uuid4())


        task = {

            "id": task_id,

            "goal": goal,

            "status": "created",

            "created_at":
                datetime.now().isoformat()

        }


        self.tasks[task_id] = task


        event_bus.publish(

            "task_created",

            "Kernel",

            task

        )


        logger.info(

            f"Task created: {goal}"

        )


        return task



    def update_task_status(

        self,

        task_id,

        status

    ):


        if task_id not in self.tasks:

            return {

                "status": "error",

                "message": "Task not found"

            }



        self.tasks[task_id]["status"] = status


        event_bus.publish(

            "task_updated",

            "Kernel",

            self.tasks[task_id]

        )


        return self.tasks[task_id]



    def get_task(self, task_id):

        return self.tasks.get(task_id)



    def system_status(self):


        health_monitor.update_status(

            "Kernel",

            "healthy",

            "Kernel running"

        )


        return {


            "kernel":

                "active",


            "tasks":

                len(self.tasks),


            "time":

                datetime.now().isoformat()

        }



muthuai_kernel = MuthuAIKernel()