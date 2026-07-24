from datetime import datetime


class GoalManager:


    def __init__(self):

        self.goals = [

            {
                "area": "Wealth",
                "goal": "Build long term financial freedom",
                "priority": 1
            },

            {
                "area": "Business",
                "goal": "Build successful AI powered businesses",
                "priority": 2
            },

            {
                "area": "Career",
                "goal": "Continuous professional growth",
                "priority": 3
            },

            {
                "area": "Health",
                "goal": "Build strong body and health",
                "priority": 4
            },

            {
                "area": "Learning",
                "goal": "Continuously improve knowledge",
                "priority": 5
            },

            {
                "area": "Legacy",
                "goal": "Create meaningful impact",
                "priority": 6
            }

        ]



    def get_goals(self):

        return self.goals



    def add_goal(self, area, goal, priority):

        self.goals.append(
            {
                "area": area,
                "goal": goal,
                "priority": priority,
                "created_at": datetime.now().isoformat()
            }
        )

        return self.goals



goal_manager = GoalManager()