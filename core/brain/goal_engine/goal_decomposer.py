from datetime import datetime


class GoalDecomposer:


    def decompose(self, goal):

        goal_lower = goal.lower()

        tasks = []


        if any(word in goal_lower for word in [
            "wealth",
            "investment",
            "money",
            "finance"
        ]):

            tasks = [
                "Analyze current financial position",
                "Define financial targets",
                "Create investment strategy",
                "Plan income growth methods",
                "Build asset creation roadmap",
                "Create monitoring system"
            ]


        elif any(word in goal_lower for word in [
            "business",
            "company",
            "startup",
            "growth"
        ]):

            tasks = [
                "Analyze business model",
                "Research market opportunity",
                "Create growth strategy",
                "Build customer acquisition plan",
                "Define execution roadmap"
            ]


        elif any(word in goal_lower for word in [
            "app",
            "software",
            "ai",
            "technology"
        ]):

            tasks = [
                "Define product requirements",
                "Design system architecture",
                "Create development roadmap",
                "Build testing strategy",
                "Plan deployment"
            ]


        else:

            tasks = [
                "Understand objective",
                "Research information",
                "Create solution",
                "Execute plan",
                "Review results"
            ]


        return {

            "goal": goal,

            "generated_tasks": tasks,

            "task_count": len(tasks),

            "created_at": datetime.now().isoformat()

        }



goal_decomposer = GoalDecomposer()