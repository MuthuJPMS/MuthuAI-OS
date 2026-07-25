from datetime import datetime

from core.mission.integration.brain_mission_bridge import brain_mission_bridge


class MissionController:


    def __init__(self):

        self.bridge = brain_mission_bridge



    def handle_goal(self, goal, category="General", priority=5, agents=None):


        if agents is None:

            agents = []



        result = self.bridge.create_and_execute(

            goal,

            category,

            priority,

            agents

        )



        return {


            "controller": "Mission Controller",

            "goal": goal,

            "category": category,

            "priority": priority,

            "result": result,

            "processed_at": datetime.now().isoformat()


        }



mission_controller = MissionController()