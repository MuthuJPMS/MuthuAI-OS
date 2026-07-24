from datetime import datetime


class ExperienceStore:


    def __init__(self):

        self.experiences = []


    def save(self, task, agent, result):

        experience = {

            "task": task,

            "agent": agent,

            "result": result,

            "created_at": datetime.now().isoformat()

        }


        self.experiences.append(experience)

        return experience



    def search(self, keyword):

        keyword = keyword.lower()

        return [

            exp for exp in self.experiences

            if keyword in exp["task"].lower()

        ]



    def count(self):

        return len(self.experiences)



experience_store = ExperienceStore()