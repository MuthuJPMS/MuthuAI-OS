from datetime import datetime


class GoalManager:


    def create_goal(self, goal, timeline="long_term"):

        return {

            "goal": goal,

            "timeline": timeline,

            "status": "created",

            "created_at": datetime.now().isoformat()

        }



    def breakdown_goal(self, goal):

        goal_lower = goal.lower()


        if "wealth" in goal_lower or "investment" in goal_lower:

            milestones = [

                "Analyze financial position",

                "Create income growth strategy",

                "Build investment plan",

                "Create asset allocation",

                "Review yearly progress"

            ]


        elif "business" in goal_lower:

            milestones = [

                "Market research",

                "Business strategy",

                "Customer acquisition plan",

                "Revenue system",

                "Growth optimization"

            ]


        elif "ai" in goal_lower or "software" in goal_lower:

            milestones = [

                "Architecture planning",

                "Development roadmap",

                "Testing system",

                "Deployment plan",

                "Continuous improvement"

            ]


        else:

            milestones = [

                "Understand objective",

                "Research information",

                "Create execution plan",

                "Track progress"

            ]



        return {

            "goal": goal,

            "milestones": milestones,

            "milestone_count": len(milestones),

            "generated_at": datetime.now().isoformat()

        }



goal_manager = GoalManager()