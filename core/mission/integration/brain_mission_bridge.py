from core.mission.mission_manager import mission_manager
from core.mission.mission_planner import mission_planner
from core.mission.mission_executor import mission_executor
from core.mission.mission_status import mission_status


class BrainMissionBridge:


    def __init__(self):

        self.manager = mission_manager
        self.planner = mission_planner
        self.executor = mission_executor
        self.status = mission_status



    def create_and_execute(self, goal, category="General", priority=5, agents=None):


        if agents is None:

            agents = []



        # Create mission

        mission_data = self.manager.create_mission(
            goal,
            category,
            priority
        )



        mission = self.manager.missions[-1]



        # Create mission plan

        plan = self.planner.create_plan(
            mission.title,
            mission.category
        )



        # Add tasks

        for task in plan["tasks"]:

            mission.add_task(task)



        # Assign agents

        for agent in agents:

            mission.assign_agent(agent)



        # Execute mission

        execution = self.executor.execute(
            mission,
            mission.assigned_agents
        )



        # Save status

        status = self.status.record(
            mission
        )



        return {


            "mission": mission_data,

            "plan": plan,

            "execution": execution,

            "status": status

        }



brain_mission_bridge = BrainMissionBridge()