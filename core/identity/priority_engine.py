class PriorityEngine:


    def __init__(self):

        self.rules = {

            "wealth": 10,
            "business": 9,
            "career": 8,
            "health": 7,
            "learning": 6,
            "entertainment": 3

        }



    def evaluate(self, action):

        action = action.lower()


        score = 5


        for key, value in self.rules.items():

            if key in action:

                score = value


        return {

            "action": action,

            "priority_score": score,

            "recommendation":

            "High priority"
            if score >= 8
            else
            "Review before action"

        }



priority_engine = PriorityEngine()