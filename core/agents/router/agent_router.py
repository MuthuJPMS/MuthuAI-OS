from datetime import datetime

from core.agents.router.capability.capability_router import capability_router



class AgentRouter:


    def __init__(self):

        self.capability_router = capability_router



    def route(self, goal):


        capability_result = self.capability_router.route(goal)


        return {


            "goal": goal,


            "domain": capability_result["domain"],


            "agents": capability_result["agents"],


            "capabilities": capability_result["capabilities"],


            "routing_time": datetime.now().isoformat()


        }



agent_router = AgentRouter()