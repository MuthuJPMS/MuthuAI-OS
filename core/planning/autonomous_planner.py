from datetime import datetime


class AutonomousPlanner:


    def create_plan(self, goal_data):


        tasks = []


        for milestone in goal_data["milestones"]:

            tasks.append({

                "task": milestone,

                "priority": "medium",

                "status": "pending"

            })



        return {

            "goal": goal_data["goal"],

            "tasks": tasks,

            "total_tasks": len(tasks),

            "planning_status": "completed",

            "created_at": datetime.now().isoformat()

        }



autonomous_planner = AutonomousPlanner()