from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor

from core.agents.registry.agent_registry import agent_registry
from core.security.security_policy import security_policy



class AgentRouter:


    def __init__(self):

        health_monitor.register_component(
            "Agent Router"
        )

        logger.info(
            "Agent Router initialized"
        )



    def route(self, goal):


        goal_lower = goal.lower()


        required_capabilities = []


        if "insurance" in goal_lower:

            required_capabilities.append(
                "insurance"
            )


        if "recruit" in goal_lower:

            required_capabilities.append(
                "recruitment"
            )


        if "content" in goal_lower:

            required_capabilities.append(
                "content"
            )


        if "finance" in goal_lower:

            required_capabilities.append(
                "finance"
            )


        selected_agents = []


        for capability in required_capabilities:


            agents = agent_registry.find_by_capability(
                capability
            )


            for agent in agents:

                selected_agents.append(
                    agent["name"]
                )



        return {


            "goal": goal,

            "required_capabilities":
                required_capabilities,

            "agents":
                selected_agents,

            "routing_status":

                "completed"

        }



agent_router = AgentRouter()