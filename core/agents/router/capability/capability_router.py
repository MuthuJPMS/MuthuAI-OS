from datetime import datetime



class CapabilityRouter:


    def __init__(self):

        self.capability_map = {


            "insurance": {

                "agents": [

                    "Insurance Agent",

                    "Advisor Agent",

                    "Client Agent"

                ],

                "capabilities": [

                    "policy_management",

                    "client_management",

                    "advisor_management"

                ]

            },


            "marketing": {

                "agents": [

                    "Marketing Agent",

                    "Content Factory Agent"

                ],

                "capabilities": [

                    "content_creation",

                    "campaign_management",

                    "communication"

                ]

            },


            "finance": {

                "agents": [

                    "Finance Agent"

                ],

                "capabilities": [

                    "calculation",

                    "analysis",

                    "reporting"

                ]

            },


            "research": {

                "agents": [

                    "Research Agent"

                ],

                "capabilities": [

                    "information_search",

                    "knowledge_analysis"

                ]

            },


            "general": {

                "agents": [

                    "Personal Assistant Agent"

                ],

                "capabilities": [

                    "planning",

                    "coordination"

                ]

            }

        }



    def detect_domain(self, goal):

        goal = goal.lower()


        for domain in self.capability_map:

            if domain in goal:

                return domain


        keywords = {


            "insurance": [

                "policy",

                "advisor",

                "claim",

                "insurance",

                "customer"

            ],


            "marketing": [

                "content",

                "campaign",

                "social",

                "youtube"

            ],


            "finance": [

                "money",

                "investment",

                "wealth",

                "finance"

            ],


            "research": [

                "research",

                "analyze",

                "study"

            ]

        }


        for domain, words in keywords.items():

            for word in words:

                if word in goal:

                    return domain


        return "general"



    def route(self, goal):


        domain = self.detect_domain(goal)


        result = self.capability_map[domain]


        return {


            "goal": goal,


            "domain": domain,


            "agents": result["agents"],


            "capabilities": result["capabilities"],


            "routed_at": datetime.now().isoformat()

        }



capability_router = CapabilityRouter()