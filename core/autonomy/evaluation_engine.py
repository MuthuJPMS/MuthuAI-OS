from datetime import datetime


class EvaluationEngine:


    def evaluate(self, execution_result):

        status = execution_result.get(
            "status",
            "unknown"
        )


        if status == "Execution completed":

            score = 100
            feedback = "Task completed successfully"

        else:

            score = 50
            feedback = "Needs improvement"



        return {

            "score": score,

            "feedback": feedback,

            "improvement_required": score < 80,

            "evaluated_at": datetime.now().isoformat()

        }



evaluation_engine = EvaluationEngine()