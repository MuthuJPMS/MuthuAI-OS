from datetime import datetime


class ExecutionManager:


    def __init__(self):

        self.executions = []


    def start(self, order):

        execution = {

            "objective": order["executive_order"],

            "status": "running",

            "started_at": datetime.now().isoformat()

        }


        self.executions.append(execution)

        return execution



    def complete(self, objective):

        for item in self.executions:

            if item["objective"] == objective:

                item["status"] = "completed"

                item["completed_at"] = datetime.now().isoformat()

                return item


        return None



execution_manager = ExecutionManager()