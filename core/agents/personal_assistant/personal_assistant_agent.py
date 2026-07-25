from core.agents.base.base_agent import BaseAgent

from core.infrastructure.logger import logger

from core.agents.registry.agent_registry import agent_registry



class PersonalAssistantAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            name="Personal Assistant Agent",

            role="Personal AI Assistant",

            capabilities=[

                "planning",

                "task_management",

                "goal_tracking",

                "personal_assistance"

            ]

        )



    def run(self, task):


        logger.info(

            f"Personal Assistant processing: {task}"

        )


        task_lower = task.lower()



        if "plan" in task_lower:


            response = {

                "type": "planning",

                "message":

                    "Creating structured action plan"

            }



        elif "goal" in task_lower:


            response = {

                "type": "goal_tracking",

                "message":

                    "Analyzing goal progress"

            }



        elif "task" in task_lower:


            response = {

                "type": "task_management",

                "message":

                    "Organizing tasks"

            }



        else:


            response = {

                "type": "assistant",

                "message":

                    "Helping user with requested activity"

            }



        return response




personal_assistant_agent = PersonalAssistantAgent()



agent_registry.register_agent(

    "Personal Assistant Agent",

    personal_assistant_agent,

    [

        "planning",

        "task_management",

        "goal_tracking",

        "personal_assistance"

    ],

    "Primary personal AI assistant"

)