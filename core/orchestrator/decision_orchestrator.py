from datetime import datetime

from core.brain.context_engine.context_analyzer import context_analyzer
from core.brain.context_engine.strategy_selector import strategy_selector

from core.planning.goal_manager import goal_manager
from core.planning.autonomous_planner import autonomous_planner

from core.agents.router.agent_router import agent_router


class DecisionOrchestrator:


    def process(self, user_goal):

        print("MuthuAI Decision Orchestrator Started...")


        # 1. Understand request

        context = context_analyzer.analyze(
            user_goal
        )


        # 2. Select strategy

        strategy = strategy_selector.select(
            context
        )


        # 3. Create goal

        goal = goal_manager.create_goal(
            user_goal
        )


        # 4. Break goal

        breakdown = goal_manager.breakdown_goal(
            user_goal
        )


        # 5. Create execution plan

        plan = autonomous_planner.create_plan(
            breakdown
        )


        # 6. Route agents

        routing = agent_router.route(
            user_goal
        )


        return {

            "goal": user_goal,

            "context": context,

            "strategy": strategy,

            "goal_structure": goal,

            "plan": plan,

            "agent_routing": routing,

            "status": "Decision pipeline completed",

            "completed_at": datetime.now().isoformat()

        }



decision_orchestrator = DecisionOrchestrator()