"""
MuthuAI OS - Base Agent Engine v1

Core foundation class for all AI agents.
Every agent in MuthuAI OS will inherit this class.
"""

from datetime import datetime
from typing import Dict, Any, List


class BaseAgent:
    """
    Universal AI Agent Base Class

    All specialized agents:
    - CEO Agent
    - CTO Agent
    - Finance Agent
    - Content Agent
    - Insurance Agent

    will extend this class.
    """

    def __init__(
        self,
        name: str,
        role: str,
        description: str = "",
        tools: List[str] = None
    ):
        self.name = name
        self.role = role
        self.description = description

        self.tools = tools or []

        self.memory = []
        self.status = "initialized"

        self.created_at = datetime.now()

    # -------------------------
    # Agent Information
    # -------------------------

    def identity(self) -> Dict[str, Any]:
        """
        Returns agent profile
        """

        return {
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "tools": self.tools,
            "status": self.status
        }


    # -------------------------
    # Thinking Layer
    # -------------------------

    def think(self, task: str) -> Dict[str, Any]:
        """
        Basic reasoning layer.

        Future:
        - LLM integration
        - Planning engine
        - Decision engine
        """

        return {
            "agent": self.name,
            "thought": f"Analyzing task: {task}",
            "timestamp": datetime.now().isoformat()
        }


    # -------------------------
    # Task Execution
    # -------------------------

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Main execution pipeline
        """

        self.status = "working"

        thought = self.think(task)

        result = {
            "agent": self.name,
            "task": task,
            "result": "Task processed successfully",
            "thought": thought,
            "timestamp": datetime.now().isoformat()
        }

        self.save_memory(result)

        self.status = "completed"

        return result


    # -------------------------
    # Memory
    # -------------------------

    def save_memory(self, data: Dict[str, Any]):
        """
        Store agent memory.

        Future:
        - Vector database
        - PostgreSQL
        - Knowledge graph
        """

        self.memory.append(data)


    def get_memory(self):

        return self.memory


    # -------------------------
    # Response
    # -------------------------

    def respond(self, message: str):

        return {
            "agent": self.name,
            "response": message,
            "timestamp": datetime.now().isoformat()
        }


    # -------------------------
    # Health Check
    # -------------------------

    def health(self):

        return {
            "agent": self.name,
            "status": self.status,
            "memory_count": len(self.memory)
        }