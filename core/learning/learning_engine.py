from datetime import datetime

from core.learning.experience_store import experience_store

from core.memory.knowledge_store import knowledge_store



class LearningEngine:



    def learn(self, execution_result):


        task = execution_result.get("task")


        agents = execution_result.get(
            "executed_agents",
            []
        )


        insights = execution_result.get(
            "results",
            []
        )


        saved = []


        for agent in agents:


            experience = experience_store.save(

                task,

                agent,

                "Completed successfully"

            )


            saved.append(experience)



            knowledge_store.add(

                task,

                f"{agent} completed this task successfully",

                "Agent Experience"

            )



        return {


            "learning_status":

            "completed",


            "experiences_saved":

            len(saved),


            "learned_at":

            datetime.now().isoformat()

        }




learning_engine = LearningEngine()