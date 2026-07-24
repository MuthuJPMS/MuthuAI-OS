from datetime import datetime

from core.agents.base_agent import BaseAgent


class MultiAgentExecutor:


    def __init__(self):

        self.agents = {}


    def register_agent(self, agent):

        self.agents[agent.name] = agent


    def execute(self, agents, task):

        results = []


        for agent_name in agents:

            agent = self.agents.get(agent_name)


            if agent:

                result = agent.execute(task)

                results.append(result)


            else:

                results.append(
                    {
                        "agent": agent_name,
                        "status": "Agent not found"
                    }
                )


        return {

            "task": task,

            "executed_agents": agents,

            "results": results,

            "executed_at": datetime.now().isoformat()

        }



multi_agent_executor = MultiAgentExecutor()