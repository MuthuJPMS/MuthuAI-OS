"""
MuthuAI OS - Agent Registry v1

Central registry for all AI agents.
"""

from typing import Dict
from core.agents.base_agent import BaseAgent


class AgentRegistry:
    """
    Stores and manages all MuthuAI agents.
    """

    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}


    def register(self, agent: BaseAgent):
        """
        Add new agent
        """

        self.agents[agent.name] = agent


    def get(self, name: str):

        return self.agents.get(name)


    def list_agents(self):

        return [
            agent.identity()
            for agent in self.agents.values()
        ]


    def remove(self, name: str):

        if name in self.agents:
            del self.agents[name]


    def count(self):

        return len(self.agents)


# Global registry instance

agent_registry = AgentRegistry()