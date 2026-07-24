"""
MuthuAI OS - Decision Engine v1

Basic decision making layer.
"""


from datetime import datetime


class DecisionEngine:


    def analyze(self, task: str):

        task_lower = task.lower()


        category = "general"
        priority = "medium"
        suggested_agent = "General Agent"


        if any(
            word in task_lower
            for word in [
                "money",
                "investment",
                "finance",
                "wealth"
            ]
        ):
            category = "finance"
            suggested_agent = "Finance Agent"


        elif any(
            word in task_lower
            for word in [
                "code",
                "software",
                "app",
                "technology"
            ]
        ):
            category = "technology"
            suggested_agent = "CTO Agent"


        elif any(
            word in task_lower
            for word in [
                "business",
                "growth",
                "strategy"
            ]
        ):
            category = "business"
            suggested_agent = "CEO Agent"


        if "urgent" in task_lower:
            priority = "high"


        return {

            "task": task,

            "category": category,

            "suggested_agent": suggested_agent,

            "priority": priority,

            "timestamp": datetime.now().isoformat()

        }



decision_engine = DecisionEngine()