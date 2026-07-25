from datetime import datetime


class DependencyContainer:


    def __init__(self):

        self._services = {}



    def register(self, name, instance):

        self._services[name] = instance


        return {

            "status": "registered",

            "service": name,

            "registered_at": datetime.now().isoformat()

        }



    def resolve(self, name):

        service = self._services.get(name)


        if service is None:

            raise KeyError(

                f"Service '{name}' is not registered."

            )


        return service



    def exists(self, name):

        return name in self._services



    def unregister(self, name):


        if name in self._services:

            del self._services[name]


            return {

                "status": "removed",

                "service": name

            }


        return {

            "status": "not_found",

            "service": name

        }



    def clear(self):


        self._services.clear()


        return {

            "status": "cleared"

        }



    def list_services(self):


        return {

            "count": len(self._services),

            "services": sorted(

                self._services.keys()

            )

        }



container = DependencyContainer()