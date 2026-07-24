"""
MuthuAI OS - Agent Executor v1

Responsible for:
- Finding agent
- Executing task
- Returning result
"""

from datetime import datetime


class AgentExecutor:

    def __init__(self):
        self.execution_history = []


    def execute(self, agent, task):

        result = agent.execute(task)

        execution = {

            "agent": agent.name,

            "task": task,

            "result": result,

            "executed_at": datetime.now().isoformat()

        }


        self.execution_history.append(execution)


        return execution



    def history(self):

        return self.execution_history



agent_executor = AgentExecutor()