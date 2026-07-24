class DNARegistry:


    def __init__(self):

        self.agents = []



    def register(self, dna):

        self.agents.append(
            dna
        )

        return {

            "status": "registered",

            "agent": dna["name"]

        }



    def get_all(self):

        return self.agents



dna_registry = DNARegistry()