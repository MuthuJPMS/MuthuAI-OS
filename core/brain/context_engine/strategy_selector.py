from datetime import datetime


class StrategySelector:


    def select(self, context):

        if context["experience_count"] > 0:

            strategy = (
                "Use previous successful experience "
                "and improve execution strategy"
            )

        else:

            strategy = (
                "Create new strategy using agent planning"
            )


        return {

            "task": context["task"],

            "strategy": strategy,

            "based_on_experience":
                context["experience_count"],

            "created_at":
                datetime.now().isoformat()

        }



strategy_selector = StrategySelector()