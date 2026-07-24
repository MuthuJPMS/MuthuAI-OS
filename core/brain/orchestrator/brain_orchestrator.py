from datetime import datetime

from core.kernel.os_kernel import muthuai_kernel

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



    def process(self, goal):

        print("MuthuAI Brain Processing Started...")


        # 1. Create kernel task

        task = self.kernel.create_task(goal)



        # 2. Create workflow plan

        workflow_result = self.workflow.run(goal)



        # 3. Route agents

        routing = self.router.route(goal)



        # 4. Execute selected agents

        execution = self.executor.execute(
            routing["agents"],
            goal
        )



        # 5. Merge results

        report = self.merger.merge(
            execution
        )



        # 6. Save memory

        for agent in routing["agents"]:

            self.memory.save_execution(
                goal,
                agent,
                "Completed execution"
            )



        # 7. Learning

        self.learning.learn(
            {
                "task": goal,
                "executed_agents": routing["agents"],
                "results": execution
            }
        )



        # 8. Final response

        final_result = {

            "goal": goal,

            "task": task,

            "workflow": workflow_result,

            "routing": routing,

            "report": report,

            "status": "completed",

            "completed_at": datetime.now().isoformat()

        }


        return final_result



brain_orchestrator = BrainOrchestrator()