from datetime import datetime


class MuthuProfile:


    def __init__(self):

        self.profile = {

            "name": "Muthu",

            "mission":
            "Build wealth, growth, businesses and a better life with AI assistance",

            "values":
            [
                "Growth",
                "Freedom",
                "Learning",
                "Family",
                "Legacy"
            ],

            "privacy_rules":
            {
                "personal_data": "private",
                "publish": "approval_required"
            },

            "created_at":
            datetime.now().isoformat()

        }



    def get_profile(self):

        return self.profile



    def update_value(self, key, value):

        self.profile[key] = value

        return self.profile



muthu_profile = MuthuProfile()