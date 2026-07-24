from core.storage.sqlite_manager import sqlite_manager


class RetrievalEngine:


    def search_memory(
        self,
        keyword
    ):

        memories = sqlite_manager.get_memories()


        results = []


        for memory in memories:

            if keyword.lower() in str(memory).lower():

                results.append(memory)


        return {
            "keyword": keyword,
            "matches": results,
            "count": len(results)
        }



retrieval_engine = RetrievalEngine()