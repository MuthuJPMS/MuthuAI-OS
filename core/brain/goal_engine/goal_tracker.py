from datetime import datetime


class GoalTracker:


    def __init__(self):

        self.goals = []


    def create_goal(self, goal):

        data = {

            "goal": goal,

            "status": "created",

            "progress": 0,

            "created_at": datetime.now().isoformat()

        }


        self.goals.append(data)

        return data



    def update_progress(self, goal, progress):

        for item in self.goals:

            if item["goal"] == goal:

                item["progress"] = progress

                item["status"] = "in_progress"

                return item


        return None



    def list_goals(self):

        return self.goals



goal_tracker = GoalTracker()