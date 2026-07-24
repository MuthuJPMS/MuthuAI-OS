from datetime import datetime

from core.brain.context_engine.context_analyzer import context_analyzer
from core.brain.goal_engine.goal_decomposer import goal_decomposer
from core.brain.task_planner import task_planner


class MissionController:


    def create_mission(self, objective):

        context = context_analyzer.analyze(
            objective
        )


        goal_plan = goal_decomposer.decompose(
            objective
        )


        task_plan = task_planner.create_plan(
            objective
        )


        return {

            "mission": objective,

            "context": context,

            "goal_plan": goal_plan,

            "execution_plan": task_plan,

            "status": "created",

            "created_at": datetime.now().isoformat()

        }



mission_controller = MissionController()