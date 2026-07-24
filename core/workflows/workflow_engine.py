"""
MuthuAI OS - Workflow Engine v1

Connects:
Decision Engine
Task Planner
Agent Manager
Memory Manager
"""

from datetime import datetime

from core.brain.decision_engine import decision_engine
from core.brain.task_planner import task_planner
from core.memory.memory_manager import memory_manager


class WorkflowEngine:

    def run(self, goal):

        print("Starting Workflow...")

        # Step 1: Analyze goal
        decision = decision_engine.analyze(goal)


        # Step 2: Create task plan
        plan = task_planner.create_plan(goal)


        # Step 3: Save workflow memory
        memory_manager.remember(
            {
                "goal": goal,
                "decision": decision,
                "plan": plan
            },
            "long"
        )


        return {

            "goal": goal,

            "decision": decision,

            "plan": plan,

            "status": "Workflow completed",

            "completed_at": datetime.now().isoformat()

        }



workflow_engine = WorkflowEngine()