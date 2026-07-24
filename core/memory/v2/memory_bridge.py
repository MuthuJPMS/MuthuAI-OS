from datetime import datetime

from core.storage.sqlite_manager import sqlite_manager


class MemoryBridge:


    def save_execution(
        self,
        task,
        agent,
        result
    ):

        memory_data = {
            "task": task,
            "agent": agent,
            "result": result,
            "saved_at": datetime.now().isoformat()
        }


        sqlite_manager.save_memory(
            str(memory_data),
            "agent_execution"
        )


        return {
            "status": "saved",
            "memory": memory_data
        }



    def save_learning(
        self,
        learning
    ):

        sqlite_manager.save_memory(
            learning,
            "learning"
        )


        return {
            "status": "learning_saved",
            "data": learning
        }



memory_bridge = MemoryBridge()