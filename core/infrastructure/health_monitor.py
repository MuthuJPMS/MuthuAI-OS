from datetime import datetime


class HealthMonitor:


    def __init__(self):

        self.components = {}



    def register_component(self, name):

        self.components[name] = {

            "status": "healthy",

            "last_check": datetime.now().isoformat(),

            "message": "Component initialized"

        }



    def update_status(

        self,

        name,

        status,

        message=""

    ):

        if name not in self.components:

            self.register_component(name)


        self.components[name] = {

            "status": status,

            "last_check": datetime.now().isoformat(),

            "message": message

        }



    def get_component(self, name):

        return self.components.get(

            name,

            None

        )



    def overall_health(self):


        unhealthy = []


        for name, info in self.components.items():

            if info["status"] != "healthy":

                unhealthy.append(

                    {

                        "component": name,

                        "status": info["status"]

                    }

                )


        return {

            "overall_status":

                "healthy"

                if len(unhealthy) == 0

                else "degraded",

            "total_components":

                len(self.components),

            "unhealthy_components":

                unhealthy,

            "checked_at":

                datetime.now().isoformat()

        }



    def all_components(self):

        return self.components



health_monitor = HealthMonitor()