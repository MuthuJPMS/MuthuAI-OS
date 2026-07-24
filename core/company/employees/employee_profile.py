from datetime import datetime


class EmployeeProfile:


    def __init__(
        self,
        name,
        role,
        department,
        skills
    ):

        self.profile = {

            "name": name,

            "role": role,

            "department": department,

            "skills": skills,

            "experience": 0,

            "performance_score": 0,

            "level": "Junior",

            "created_at": datetime.now().isoformat()

        }



    def add_experience(self, points):

        self.profile["experience"] += points

        return self.profile



    def update_performance(self, score):

        self.profile["performance_score"] = score


        if score >= 90:

            self.profile["level"] = "Senior"

        elif score >= 70:

            self.profile["level"] = "Mid Level"

        else:

            self.profile["level"] = "Junior"


        return self.profile



    def get_profile(self):

        return self.profile