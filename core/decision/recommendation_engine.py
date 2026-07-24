class RecommendationEngine:


    def __init__(self):

        self.positive_keywords = [

            "wealth",
            "business",
            "health",
            "learning",
            "growth",
            "career"

        ]



    def recommend(self, action):

        action_lower = action.lower()


        matched = []


        for keyword in self.positive_keywords:

            if keyword in action_lower:

                matched.append(keyword)



        if matched:

            decision = "aligned_with_goals"

        else:

            decision = "needs_review"



        return {

            "action": action,

            "goal_alignment": decision,

            "matched_goals": matched

        }



recommendation_engine = RecommendationEngine()