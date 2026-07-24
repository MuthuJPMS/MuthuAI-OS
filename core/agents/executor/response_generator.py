"""
MuthuAI OS - Response Generator v1

Responsible for:
- Formatting agent results
- Creating readable reports
"""


from datetime import datetime


class ResponseGenerator:


    def __init__(self):
        self.responses = []



    def generate(self, execution_result):

        response = {

            "title": "MuthuAI OS Agent Report",

            "agent": execution_result.get("agent"),

            "task": execution_result.get("task"),

            "status": "Completed",

            "result": execution_result.get("result"),

            "generated_at": datetime.now().isoformat()

        }


        self.responses.append(response)


        return response




    def history(self):

        return self.responses



response_generator = ResponseGenerator()