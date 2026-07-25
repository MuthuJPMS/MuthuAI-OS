from datetime import datetime


class MissionStatus:


    def __init__(self):

        self.status_history = []



    def record(self, mission):

        status_data = {

            "mission_id": mission.id,

            "mission": mission.title,

            "status": mission.status,

            "progress": mission.progress,

            "recorded_at": datetime.now().isoformat()

        }


        self.status_history.append(status_data)


        return status_data



    def get_status(self, mission):

        return {

            "mission": mission.title,

            "status": mission.status,

            "progress": mission.progress,

            "tasks_completed": len(mission.tasks),

            "agents": mission.assigned_agents

        }



    def history(self):

        return self.status_history



mission_status = MissionStatus()