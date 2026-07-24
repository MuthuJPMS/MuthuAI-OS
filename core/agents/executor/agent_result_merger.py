from datetime import datetime



class AgentResultMerger:


    def merge(self, execution_results):


        return {


            "title":
            "MuthuAI OS Multi Agent Report",


            "task":
            execution_results.get("task"),


            "agents":
            execution_results.get("executed_agents"),


            "insights":
            execution_results.get("results"),


            "status":
            "Multi Agent Execution Completed",


            "generated_at":
            datetime.now().isoformat()

        }



agent_result_merger = AgentResultMerger()