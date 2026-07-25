from datetime import datetime
import time
import threading


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor


from core.scheduler.scheduler_engine import scheduler_engine



class WorkerEngine:


    def __init__(self):

        self.running = False

        self.worker_thread = None

        health_monitor.register_component(
            "Worker Engine"
        )

        logger.info(
            "Worker Engine initialized"
        )



    def start(self):

        if self.running:

            return {

                "status": "already_running"

            }


        self.running = True


        self.worker_thread = threading.Thread(

            target=self._worker_loop,

            daemon=True

        )


        self.worker_thread.start()


        logger.info(

            "Worker Engine started"

        )


        return {

            "status": "started"

        }



    def stop(self):


        self.running = False


        logger.info(

            "Worker Engine stopped"

        )


        return {

            "status": "stopped"

        }



    def _worker_loop(self):


        while self.running:


            self.process_jobs()


            time.sleep(5)



    def process_jobs(self):


        jobs = scheduler_engine.list_jobs()


        for job in jobs:


            if job["status"] == "scheduled":


                logger.info(

                    f"Executing job: {job['name']}"

                )


                scheduler_engine.run_job(

                    job["id"]

                )



        health_monitor.update_status(

            "Worker Engine",

            "healthy",

            "Worker running"

        )



    def status(self):


        return {

            "running":

                self.running,

            "checked_at":

                datetime.now().isoformat()

        }



worker_engine = WorkerEngine()