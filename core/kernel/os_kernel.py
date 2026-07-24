from datetime import datetime

from core.kernel.system_state import system_state
from core.kernel.event_bus import event_bus
from core.kernel.task_manager import task_manager
from core.kernel.permission_manager import permission_manager


class MuthuAIKernel:


    def __init__(self):

        self.name = "MuthuAI OS"
        self.version = "0.1"

        self.state = system_state
        self.events = event_bus
        self.tasks = task_manager
        self.permissions = permission_manager



    def boot(self):

        self.state.update_status("running")

        event = self.events.publish(
            "SYSTEM_BOOT",
            {
                "system": self.name,
                "version": self.version
            }
        )

        return {
            "system": self.name,
            "status": "online",
            "version": self.version,
            "event": event,
            "time": datetime.now().isoformat()
        }



    def create_task(self, task):

        new_task = self.tasks.create_task(task)

        self.state.add_task()

        self.events.publish(
            "TASK_CREATED",
            new_task
        )

        return new_task



    def get_system_report(self):

        return {

            "system": self.name,

            "version": self.version,

            "state": self.state.get_state(),

            "tasks": self.tasks.get_tasks(),

            "events": self.events.get_events()

        }



    def request_permission(self, action):

        return self.permissions.request_permission(action)



muthuai_kernel = MuthuAIKernel()