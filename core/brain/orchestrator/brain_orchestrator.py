from datetime import datetime

from core.decision.decision_engine import decision_engine

from core.kernel.os_kernel import muthuai_kernel

from core.mission.integration.brain_mission_bridge import brain_mission_bridge

from core.workflows.workflow_engine import workflow_engine

from core.agents.router.agent_router import agent_router

from core.agents.executor.multi_agent_executor import multi_agent_executor

from core.agents.executor.agent_result_merger import agent_result_merger

from core.memory.v2.memory_bridge import memory_bridge

from core.learning.learning_engine import learning_engine


class BrainOrchestrator:


    def __init__(self):

        self.kernel = muthuai_kernel

        self.workflow = workflow_engine

        self.router = agent_router

        self.executor = multi_agent_executor

        self.merger = agent_result_merger

        self.memory = memory_bridge

        self.learning = learning_engine

        self.decision = decision_engine

        self.mission = brain_mission_bridge



    def process(self, goal):

        print("MuthuAI Brain Processing Started...")


        # Decision Layer

        decision_result = self.decision.evaluate(goal)


        if decision_result["final_decision"] == "approval_required":

            return {

                "status": "waiting_for_approval",

                "decision": decision_result

            }



        # Mission Layer

        mission_result = self.mission.create_and_execute(

            goal,

            "General",

            5,

            []

        )



        # Kernel Task

        task = self.kernel.create_task(goal)



        # Workflow

        workflow_result = self.workflow.run(goal)



        # Agent Routing

        routing = self.router.route(goal)



        # Agent Execution

        execution = self.executor.execute(

            routing["agents"],

            goal

        )



        # Merge Result

        report = self.merger.merge(

            execution

        )



        # Memory Save

        for agent in routing["agents"]:

            self.memory.save_execution(

                goal,

                agent,

                "Completed execution"

            )



        # Learning

        self.learning.learn(

            {

                "task": goal,

                "agents": routing["agents"],

                "results": execution

            }

        )



        final_result = {


            "goal": goal,

            "decision": decision_result,

            "mission": mission_result,

            "task": task,

            "workflow": workflow_result,

            "routing": routing,

            "report": report,

            "status": "completed",

            "completed_at": datetime.now().isoformat()

        }


        return final_result



brain_orchestrator = BrainOrchestrator()