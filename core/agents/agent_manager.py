"""
MuthuAI OS - Agent Manager v1

Central controller for managing AI agents.
"""

from core.agents.agent_registry import agent_registry


class AgentManager:

    def __init__(self):
        self.registry = agent_registry


    def add_agent(self, agent):
        """
        Register new agent
        """

        self.registry.register(agent)


    def get_agent(self, name):
        """
        Retrieve agent
        """

        return self.registry.get(name)


    def available_agents(self):

        return self.registry.list_agents()


    def run_task(self, agent_name, task):
        """
        Execute task using selected agent
        """

        agent = self.get_agent(agent_name)

        if not agent:
            return {
                "error": f"Agent {agent_name} not found"
            }


        return agent.execute(task)


# Global manager

agent_manager = AgentManager()