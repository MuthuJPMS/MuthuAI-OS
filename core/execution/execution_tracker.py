from datetime import datetime


class ExecutionTracker:


    def __init__(self):

        self.history = []



    def record(self, task, result):

        execution = {

            "task": task,

            "result": result,

            "status": "completed",

            "completed_at": datetime.now().isoformat()

        }


        self.history.append(execution)


        return execution



    def get_history(self):

        return self.history



execution_tracker = ExecutionTracker()