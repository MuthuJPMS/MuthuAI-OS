class RiskAnalyzer:


    def __init__(self):

        self.high_risk_actions = [

            "money",
            "payment",
            "investment",
            "delete",
            "publish",
            "legal"

        ]



    def analyze(self, action):

        action_lower = action.lower()

        risks = []

        for item in self.high_risk_actions:

            if item in action_lower:
                risks.append(item)


        if risks:

            return {

                "risk_level": "high",

                "requires_approval": True,

                "detected_risks": risks

            }


        return {

            "risk_level": "low",

            "requires_approval": False,

            "detected_risks": []

        }



risk_analyzer = RiskAnalyzer()