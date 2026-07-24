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

from datetime import datetime


class ContextAnalyzer:

    def analyze(self, task):

        task_lower = task.lower()

        category = "general"

        if any(word in task_lower for word in [
            "money",
            "investment",
            "wealth",
            "finance",
            "salary"
        ]):
            category = "finance"


        elif any(word in task_lower for word in [
            "insurance",
            "advisor",
            "policy",
            "sales"
        ]):
            category = "insurance"


        elif any(word in task_lower for word in [
            "code",
            "software",
            "app",
            "technology",
            "system"
        ]):
            category = "technology"


        elif any(word in task_lower for word in [
            "marketing",
            "content",
            "youtube",
            "brand"
        ]):
            category = "marketing"



        complexity = "medium"

        if len(task.split()) > 10:
            complexity = "high"


        return {

            "task": task,

            "category": category,

            "complexity": complexity,

            "requires_memory": True,

            "requires_agents": True,

            "analyzed_at": datetime.now().isoformat()

        }



context_analyzer = ContextAnalyzer()