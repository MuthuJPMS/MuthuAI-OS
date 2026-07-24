class CompanyRegistry:


    def __init__(self):

        self.company = {

            "name": "MuthuAI Virtual Company",

            "departments": []

        }



    def register(self, department):

        self.company["departments"].append(
            department
        )

        return self.company



    def overview(self):

        return self.company



company_registry = CompanyRegistry()