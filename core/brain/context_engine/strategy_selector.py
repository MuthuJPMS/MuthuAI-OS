from datetime import datetime


class StrategySelector:


    def select(self, context):

        category = context.get("category")


        strategies = {

            "finance":
                {
                    "approach": "Analyze goals, risk, assets and create wealth roadmap",
                    "agents": [
                        "Finance Agent",
                        "CEO Agent"
                    ]
                },


            "business":
                {
                    "approach": "Create execution strategy, marketing and growth plan",
                    "agents": [
                        "Business Agent",
                        "Marketing Agent",
                        "CEO Agent"
                    ]
                },


            "technology":
                {
                    "approach": "Design architecture, development roadmap and automation",
                    "agents": [
                        "CTO Agent",
                        "Developer Agent"
                    ]
                },


            "general":
                {
                    "approach": "Analyze task and create optimized solution",
                    "agents": [
                        "CEO Agent"
                    ]
                }

        }


        result = strategies.get(
            category,
            strategies["general"]
        )


        return {
            "category": category,
            "strategy": result["approach"],
            "assigned_agents": result["agents"],
            "selected_at": datetime.now().isoformat()
        }



strategy_selector = StrategySelector()