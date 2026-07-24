from datetime import datetime


class PerformanceEngine:


    def __init__(self):

        self.scores = []



    def evaluate(
        self,
        employee,
        task_success,
        quality,
        learning
    ):

        score = (
            task_success +
            quality +
            learning
        ) / 3


        record = {

            "employee": employee,

            "score": round(score,2),

            "evaluated_at": datetime.now().isoformat()

        }


        self.scores.append(record)

        return record



    def history(self):

        return self.scores



performance_engine = PerformanceEngine()