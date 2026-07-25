from datetime import datetime
import uuid


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor

from core.security.security_policy import security_policy
from core.security.audit_logger import audit_logger



class BaseAgent:


    def __init__(

        self,

        name,

        role,

        capabilities

    ):


        self.id = str(uuid.uuid4())

        self.name = name

        self.role = role

        self.capabilities = capabilities

        self.status = "initialized"


        health_monitor.register_component(

            f"Agent:{self.name}"

        )


        logger.info(

            f"Agent initialized: {self.name}"

        )



    def get_identity(self):

        return {

            "id": self.id,

            "name": self.name,

            "role": self.role,

            "capabilities": self.capabilities,

            "status": self.status

        }



    def can_execute(

        self,

        action

    ):


        result = security_policy.check_action(

            self.name,

            action

        )


        audit_logger.record(

            self.name,

            action,

            "allowed"
            if result["allowed"]
            else "blocked",

            result

        )


        return result



    def execute(

        self,

        task

    ):


        self.status = "running"


        logger.info(

            f"{self.name} executing task"

        )


        result = self.run(task)


        self.status = "completed"


        return {

            "agent": self.name,

            "task": task,

            "result": result,

            "completed_at":
                datetime.now().isoformat()

        }



    def run(

        self,

        task

    ):


        raise NotImplementedError(

            "Agent must implement run() method"

        )



    def learn(

        self,

        feedback

    ):


        logger.info(

            f"{self.name} learning from feedback"

        )


        return {

            "agent": self.name,

            "learning":

                feedback,

            "time":

                datetime.now().isoformat()

        }



    def health_check(self):


        health_monitor.update_status(

            f"Agent:{self.name}",

            "healthy",

            "Agent operational"

        )


        return self.get_identity()