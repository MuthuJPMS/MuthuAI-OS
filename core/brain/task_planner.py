"""
MuthuAI OS - Task Planner v1.1

Goal decomposition engine.
"""

from datetime import datetime


class TaskPlanner:

    def create_plan(self, goal: str):

        tasks = []

        goal_lower = goal.lower()


        # Finance / Wealth priority check
        if any(
            word in goal_lower
            for word in [
                "investment",
                "wealth",
                "money",
                "finance",
                "asset"
            ]
        ):

            tasks = [
                "Analyze financial goals",
                "Create investment strategy",
                "Plan asset allocation",
                "Review risk factors",
                "Create long term wealth roadmap"
            ]


        # Business check
        elif any(
            word in goal_lower
            for word in [
                "business",
                "startup",
                "company",
                "growth"
            ]
        ):

            tasks = [
                "Analyze current business position",
                "Create growth strategy",
                "Build marketing plan",
                "Create execution roadmap",
                "Track performance metrics"
            ]


        # Technology check
        elif any(
            word in goal_lower
            for word in [
                "software",
                "app",
                "technology",
                "code"
            ]
        ):

            tasks = [
                "Define product requirements",
                "Design architecture",
                "Develop application",
                "Testing",
                "Deployment"
            ]


        else:

            tasks = [
                "Understand objective",
                "Research information",
                "Create solution",
                "Execute plan"
            ]


        return {

            "goal": goal,
            "tasks": tasks,
            "task_count": len(tasks),
            "created_at": datetime.now().isoformat()

        }



task_planner = TaskPlanner()