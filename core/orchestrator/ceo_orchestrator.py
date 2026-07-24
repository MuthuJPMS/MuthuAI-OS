from datetime import datetime

from core.agents.router.agent_router import agent_router
from core.missions.mission_controller import mission_controller


class CEOOrchestrator:


    def create_execution(self, objective):


        mission = mission_controller.create_mission(
            objective
        )


        routing = agent_router.route(
            objective
        )


        return {

            "executive_order": objective,

            "mission": mission,

            "agent_strategy": routing,

            "status": "ready_for_execution",

            "created_at": datetime.now().isoformat()

        }



ceo_orchestrator = CEOOrchestrator()