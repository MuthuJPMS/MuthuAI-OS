"""
MuthuAI OS - Knowledge Store v1

Stores structured knowledge for AI agents.
"""


from datetime import datetime


class KnowledgeStore:

    def __init__(self):

        self.knowledge = []


    def add(
        self,
        topic: str,
        content: str,
        category: str = "general"
    ):

        item = {
            "topic": topic,
            "content": content,
            "category": category,
            "created_at": datetime.now().isoformat()
        }

        self.knowledge.append(item)

        return item


    def search(self, keyword: str):

        results = []

        for item in self.knowledge:

            text = (
                item["topic"]
                + " "
                + item["content"]
            ).lower()

            if keyword.lower() in text:
                results.append(item)

        return results


    def all(self):

        return self.knowledge


    def count(self):

        return len(self.knowledge)


# Global knowledge store

knowledge_store = KnowledgeStore()