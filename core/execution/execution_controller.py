from datetime import datetime

from core.agents.executor.multi_agent_executor import multi_agent_executor
from core.agents.executor.agent_result_merger import agent_result_merger

from core.execution.execution_tracker import execution_tracker


class ExecutionController:



    def execute(self, agents, task):


        print("MuthuAI Execution Controller Started...")


        # Execute agents

        results = multi_agent_executor.execute(

            agents,

            task

        )


        # Merge results

        report = agent_result_merger.merge(

            results

        )


        # Track execution

        execution = execution_tracker.record(

            task,

            report

        )


        return {


            "task": task,


            "agents": agents,


            "execution": execution,


            "report": report,


            "status": "Execution completed",


            "completed_at": datetime.now().isoformat()


        }




execution_controller = ExecutionController()