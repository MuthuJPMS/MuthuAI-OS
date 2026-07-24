from datetime import datetime


class ContextAnalyzer:

    def analyze(self, task):

        task_lower = task.lower()

        category = "general"
        complexity = "medium"

        if any(word in task_lower for word in [
            "money",
            "investment",
            "finance",
            "wealth",
            "asset"
        ]):
            category = "finance"

        elif any(word in task_lower for word in [
            "insurance",
            "advisor",
            "policy",
            "sales"
        ]):
            category = "business"

        elif any(word in task_lower for word in [
            "code",
            "software",
            "app",
            "technology"
        ]):
            category = "technology"


        if len(task.split()) > 8:
            complexity = "high"


        return {
            "task": task,
            "category": category,
            "complexity": complexity,
            "context_time": datetime.now().isoformat()
        }


context_analyzer = ContextAnalyzer()