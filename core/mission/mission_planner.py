from datetime import datetime


class MissionPlanner:


    def __init__(self):

        self.planning_rules = {

            "Business": [
                "Research market",
                "Create strategy",
                "Execute marketing",
                "Measure results"
            ],

            "Wealth": [
                "Analyze finances",
                "Create investment plan",
                "Track progress",
                "Optimize strategy"
            ],

            "Health": [
                "Analyze current health",
                "Create improvement plan",
                "Track habits",
                "Review progress"
            ],

            "General": [
                "Understand objective",
                "Create action plan",
                "Execute tasks",
                "Review outcome"
            ]

        }



    def create_plan(self, mission_title, category="General"):


        tasks = self.planning_rules.get(

            category,

            self.planning_rules["General"]

        )


        plan = {


            "mission": mission_title,


            "category": category,


            "tasks": tasks,


            "task_count": len(tasks),


            "planned_at": datetime.now().isoformat()


        }


        return plan



mission_planner = MissionPlanner()