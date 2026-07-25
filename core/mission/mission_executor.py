from datetime import datetime


class MissionExecutor:


    def __init__(self):

        self.execution_history = []



    def execute(self, mission, agents=None):

        if agents is None:

            agents = []


        mission.start()


        result = {


            "mission_id": mission.id,


            "mission": mission.title,


            "status": "executing",


            "agents": agents,


            "started_at": datetime.now().isoformat(),


            "steps_completed": []

        }



        for task in mission.tasks:

            result["steps_completed"].append(

                {

                    "task": task,

                    "status": "completed"

                }

            )


        mission.update_progress(100)


        result["status"] = "completed"

        result["completed_at"] = datetime.now().isoformat()



        self.execution_history.append(result)



        return result



    def get_history(self):

        return self.execution_history



mission_executor = MissionExecutor()