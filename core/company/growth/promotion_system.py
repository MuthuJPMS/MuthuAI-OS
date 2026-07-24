from datetime import datetime


class PromotionSystem:


    def promote(
        self,
        employee,
        score
    ):


        if score >= 90:

            level = "Department Head"


        elif score >= 75:

            level = "Senior Specialist"


        elif score >= 50:

            level = "Specialist"


        else:

            level = "Junior"



        return {

            "employee": employee,

            "new_level": level,

            "promoted_at": datetime.now().isoformat()

        }



promotion_system = PromotionSystem()