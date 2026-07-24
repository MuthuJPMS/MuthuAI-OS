from datetime import datetime

from core.memory.v2.retrieval_engine import retrieval_engine


class ContextAnalyzer:


    def analyze(self, task):

        keywords = task.split()

        matches = []

        for keyword in keywords:

            result = retrieval_engine.search_memory(
                keyword
            )

            if result["count"] > 0:
                matches.extend(
                    result["matches"]
                )


        return {
            "task": task,
            "previous_experiences": matches,
            "experience_count": len(matches),
            "analyzed_at": datetime.now().isoformat()
        }



context_analyzer = ContextAnalyzer()