from datetime import datetime


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor



class AgentRegistry:


    def __init__(self):

        self.agents = {}


        health_monitor.register_component(
            "Agent Registry"
        )


        logger.info(
            "Agent Registry initialized"
        )



    def register_agent(

        self,

        name,

        agent_instance,

        capabilities,

        description=""

    ):


        self.agents[name] = {


            "name": name,

            "instance": agent_instance,

            "capabilities": capabilities,

            "description": description,

            "status": "active",

            "registered_at":
                datetime.now().isoformat()

        }


        logger.info(

            f"Agent registered: {name}"

        )


        return self.agents[name]



    def unregister_agent(

        self,

        name

    ):


        if name in self.agents:

            del self.agents[name]


            return {

                "status": "removed",

                "agent": name

            }


        return {

            "status": "not_found",

            "agent": name

        }



    def get_agent(

        self,

        name

    ):


        agent = self.agents.get(name)


        if agent:

            return agent["instance"]


        return None



    def find_by_capability(

        self,

        capability

    ):


        results = []


        for name, agent in self.agents.items():


            if capability in agent["capabilities"]:


                results.append(agent)



        return results



    def list_agents(self):

        return {


            "count": len(self.agents),


            "agents": [

                {

                    "name": agent["name"],

                    "capabilities":
                        agent["capabilities"],

                    "status":
                        agent["status"]

                }

                for agent in self.agents.values()

            ]

        }



    def health_check(self):


        health_monitor.update_status(

            "Agent Registry",

            "healthy",

            f"{len(self.agents)} agents registered"

        )


        return self.list_agents()



agent_registry = AgentRegistry()