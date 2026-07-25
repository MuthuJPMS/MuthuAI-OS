from datetime import datetime


from core.infrastructure.logger import logger



class SecurityPolicy:


    def __init__(self):

        self.policies = {}

        self.load_default_policies()



    def load_default_policies(self):


        self.policies = {


            "Brain Agent": {

                "allowed": [

                    "plan",

                    "analyze",

                    "coordinate"

                ],

                "restricted": [

                    "external_action"

                ]

            },


            "Finance Agent": {

                "allowed": [

                    "read_finance",

                    "generate_report"

                ],

                "restricted": [

                    "transfer_money",

                    "make_payment"

                ]

            },


            "Content Agent": {

                "allowed": [

                    "create_content",

                    "generate_script"

                ],

                "restricted": [

                    "publish_content"

                ]

            },


            "Memory Agent": {

                "allowed": [

                    "store_memory",

                    "retrieve_memory"

                ],

                "restricted": [

                    "delete_memory"

                ]

            }


        }



    def check_action(

        self,

        agent,

        action

    ):


        policy = self.policies.get(agent)


        if not policy:


            return {

                "allowed": False,

                "reason": "Unknown agent"

            }



        if action in policy["allowed"]:


            return {

                "allowed": True,

                "reason": "Action permitted"

            }



        if action in policy["restricted"]:


            return {

                "allowed": False,

                "reason": "Approval required"

            }



        return {

            "allowed": False,

            "reason": "Action not defined"

        }



    def add_policy(

        self,

        agent,

        allowed,

        restricted

    ):


        self.policies[agent] = {


            "allowed": allowed,

            "restricted": restricted,

            "created_at":
                datetime.now().isoformat()

        }



        logger.info(

            f"Security policy added for {agent}"

        )



    def get_policy(self, agent):

        return self.policies.get(agent)



security_policy = SecurityPolicy()