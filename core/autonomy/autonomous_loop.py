from datetime import datetime

from core.orchestrator.decision_orchestrator import decision_orchestrator

from core.execution.execution_controller import execution_controller

from core.autonomy.evaluation_engine import evaluation_engine



class AutonomousLoop:


    def run(self, goal):


        print(
            "MuthuAI Autonomous Loop Started..."
        )


        # 1. Think + Plan

        decision = decision_orchestrator.process(
            goal
        )


        # 2. Get agents

        agents = decision["agent_routing"]["agents"]


        # 3. Execute

        execution = execution_controller.execute(

            agents,

            goal

        )


        # 4. Evaluate

        evaluation = evaluation_engine.evaluate(

            execution

        )


        return {


            "goal": goal,


            "decision": decision,


            "execution": execution,


            "evaluation": evaluation,


            "loop_status": "completed",


            "completed_at": datetime.now().isoformat()

        }




autonomous_loop = AutonomousLoop()