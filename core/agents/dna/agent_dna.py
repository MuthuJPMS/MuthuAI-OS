from datetime import datetime


class AgentDNA:


    def __init__(
        self,
        name,
        role,
        department,
        personality,
        decision_style,
        specialization,
        strengths,
        weaknesses
    ):

        self.dna = {

            "name": name,

            "role": role,

            "department": department,

            "personality": personality,

            "decision_style": decision_style,

            "specialization": specialization,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "created_at": datetime.now().isoformat()

        }



    def profile(self):

        return self.dna



agent_dna = AgentDNA