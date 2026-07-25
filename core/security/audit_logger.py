from datetime import datetime
import uuid


from core.infrastructure.logger import logger



class AuditLogger:


    def __init__(self):

        self.logs = []


        logger.info(
            "Audit Logger initialized"
        )



    def record(

        self,

        actor,

        action,

        result,

        details=None

    ):


        entry = {


            "id": str(uuid.uuid4()),

            "actor": actor,

            "action": action,

            "result": result,

            "details": details or {},

            "timestamp":
                datetime.now().isoformat()

        }


        self.logs.append(entry)


        logger.info(

            f"Audit: {actor} -> {action} -> {result}"

        )


        return entry



    def get_logs(self):

        return self.logs



    def search(

        self,

        actor=None,

        action=None

    ):


        results = []


        for log in self.logs:


            if actor and log["actor"] != actor:

                continue


            if action and log["action"] != action:

                continue


            results.append(log)


        return results



audit_logger = AuditLogger()