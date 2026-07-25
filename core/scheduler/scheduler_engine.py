from datetime import datetime, timedelta
import uuid


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor

from core.events.event_bus import event_bus



class SchedulerEngine:


    def __init__(self):

        self.jobs = {}

        health_monitor.register_component(
            "Scheduler"
        )

        logger.info(
            "Scheduler Engine initialized"
        )



    def add_job(
        self,
        name,
        action,
        schedule_type="once",
        run_at=None,
        interval_minutes=None
    ):


        job_id = str(uuid.uuid4())


        job = {

            "id": job_id,

            "name": name,

            "action": action,

            "schedule_type": schedule_type,

            "run_at": run_at,

            "interval_minutes": interval_minutes,

            "status": "scheduled",

            "created_at":
                datetime.now().isoformat()

        }


        self.jobs[job_id] = job


        event_bus.publish(

            "job_created",

            "Scheduler",

            job

        )


        logger.info(

            f"Scheduled job created: {name}"

        )


        return job



    def run_job(self, job_id):


        job = self.jobs.get(job_id)


        if not job:

            return {

                "status": "error",

                "message": "Job not found"

            }



        try:

            result = job["action"]()


            job["status"] = "completed"

            job["result"] = result

            job["completed_at"] = (
                datetime.now().isoformat()
            )


            event_bus.publish(

                "job_completed",

                "Scheduler",

                job

            )


            return job



        except Exception as error:


            job["status"] = "failed"

            job["error"] = str(error)


            event_bus.publish(

                "job_failed",

                "Scheduler",

                job

            )


            logger.error(

                str(error)

            )


            return job



    def list_jobs(self):

        return list(
            self.jobs.values()
        )



    def system_check(self):


        health_monitor.update_status(

            "Scheduler",

            "healthy",

            "Scheduler running"

        )


        return {

            "scheduler":

                "active",

            "jobs":

                len(self.jobs)

        }



scheduler_engine = SchedulerEngine()