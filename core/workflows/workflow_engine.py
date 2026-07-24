"""
MuthuAI OS - Workflow Engine v2

Full Autonomous Pipeline:

Goal
 ↓
Decision Engine
 ↓
Task Planner
 ↓
Agent Executor
 ↓
Response Generator
 ↓
Memory Manager
"""


from datetime import datetime

from core.brain.decision_engine import decision_engine
from core.brain.task_planner import task_planner

from core.agents.base_agent import BaseAgent

from core.agents.executor.agent_executor import agent_executor
from core.agents.executor.response_generator import response_generator

from core.memory.memory_manager import memory_manager



class WorkflowEngine:


    def __init__(self):

        self.agents = {

            "finance": BaseAgent(
                name="Finance Agent",
                role="Wealth Management"
            ),

            "insurance": BaseAgent(
                name="Insurance Agent",
                role="Insurance Strategy"
            ),

            "content": BaseAgent(
                name="Content Agent",
                role="Content Creation"
            )

        }




    def select_agent(self, category):

        return self.agents.get(
            category,
            self.agents["content"]
        )





    def run(self, goal):


        print("MuthuAI Workflow Started...")


        # 1. Decision

        decision = decision_engine.analyze(goal)



        # 2. Planning

        plan = task_planner.create_plan(goal)



        # 3. Agent Selection

        agent = self.select_agent(
            decision["category"]
        )



        # 4. Agent Execution

        execution = agent_executor.execute(

            agent,

            goal

        )



        # 5. Response Generation

        report = response_generator.generate(
            execution
        )



        # 6. Memory Save

        memory_manager.remember(

            report,

            "long"

        )



        return {

            "goal": goal,

            "decision": decision,

            "plan": plan,

            "agent": agent.identity(),

            "execution": execution,

            "report": report,

            "status": "completed",

            "completed_at": datetime.now().isoformat()

        }




workflow_engine = WorkflowEngine()