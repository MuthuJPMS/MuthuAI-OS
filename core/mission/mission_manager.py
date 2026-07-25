from core.mission.mission import Mission


class MissionManager:


    def __init__(self):

        self.missions = []



    def create_mission(self, title, category="General", priority=5):

        mission = Mission(
            title,
            category,
            priority
        )

        self.missions.append(mission)

        return mission.to_dict()



    def get_mission(self, mission_id):

        for mission in self.missions:

            if mission.id == mission_id:

                return mission.to_dict()

        return None



    def start_mission(self, mission_id):

        for mission in self.missions:

            if mission.id == mission_id:

                mission.start()

                return mission.to_dict()

        return None



    def update_mission_progress(self, mission_id, progress):

        for mission in self.missions:

            if mission.id == mission_id:

                mission.update_progress(progress)

                return mission.to_dict()

        return None



    def list_missions(self):

        return [

            mission.to_dict()

            for mission in self.missions

        ]



mission_manager = MissionManager()