from datetime import datetime


class PerformanceTracker:


    def __init__(self):

        self.records = []



    def record(
        self,
        employee,
        task,
        result
    ):

        data = {

            "employee": employee,

            "task": task,

            "result": result,

            "recorded_at": datetime.now().isoformat()

        }


        self.records.append(data)

        return data



    def history(self):

        return self.records



performance_tracker = PerformanceTracker()