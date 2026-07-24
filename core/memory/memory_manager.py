"""
MuthuAI OS - Memory Manager v1

Central memory layer for AI agents.
"""

from datetime import datetime


class MemoryManager:

    def __init__(self):
        self.short_term = []
        self.long_term = []


    def remember(self, data, memory_type="short"):

        memory = {
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        if memory_type == "long":
            self.long_term.append(memory)
        else:
            self.short_term.append(memory)


        return memory


    def recall_short_term(self):

        return self.short_term


    def recall_long_term(self):

        return self.long_term


    def clear_short_term(self):

        self.short_term = []


    def memory_stats(self):

        return {
            "short_term_count": len(self.short_term),
            "long_term_count": len(self.long_term)
        }


# Global Memory Instance

memory_manager = MemoryManager()