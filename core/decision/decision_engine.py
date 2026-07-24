from datetime import datetime

from core.decision.risk_analyzer import risk_analyzer

from core.decision.recommendation_engine import recommendation_engine



class DecisionEngine:


    def __init__(self):

        self.risk = risk_analyzer

        self.recommendation = recommendation_engine



    def evaluate(self, action):


        risk_result = self.risk.analyze(action)


        recommendation = self.recommendation.recommend(action)



        if risk_result["requires_approval"]:

            final = "approval_required"

        elif recommendation["goal_alignment"] == "aligned_with_goals":

            final = "recommended"

        else:

            final = "review"



        return {


            "action": action,

            "risk": risk_result,

            "recommendation": recommendation,

            "final_decision": final,

            "evaluated_at": datetime.now().isoformat()


        }



decision_engine = DecisionEngine()