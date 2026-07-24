from datetime import datetime


class TrainingEngine:


    def __init__(self):

        self.training_history = []


    def train(
        self,
        employee,
        skill,
        knowledge
    ):

        record = {

            "employee": employee,

            "skill_added": skill,

            "knowledge": knowledge,

            "trained_at": datetime.now().isoformat()

        }


        self.training_history.append(record)

        return record



    def history(self):

        return self.training_history



training_engine = TrainingEngine()