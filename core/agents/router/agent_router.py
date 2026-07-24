from datetime import datetime

from core.agents.router.routing_rules import find_agents



class AgentRouter:


    def route(self, task):

        agents = find_agents(task)


        return {

            "task": task,

            "agents": agents,

            "primary_agent": agents[0],

            "agent_count": len(agents),

            "routed_at": datetime.now().isoformat()

        }



agent_router = AgentRouter()