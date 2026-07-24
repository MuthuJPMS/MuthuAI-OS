from datetime import datetime


class MissionTracker:


    def __init__(self):

        self.missions = []


    def add(self, mission):

        self.missions.append(
            mission
        )

        return {
            "status": "saved",
            "mission": mission["mission"],
            "time": datetime.now().isoformat()
        }


    def update_status(self, mission_name, status):

        for mission in self.missions:

            if mission["mission"] == mission_name:

                mission["status"] = status

                return mission


        return None



    def list(self):

        return self.missions



mission_tracker = MissionTracker()