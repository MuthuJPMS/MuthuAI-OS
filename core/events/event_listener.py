from datetime import datetime



class EventListener:


    def __init__(self, name):

        self.name = name

        self.received_events = []



    def handle(self, event):

        self.received_events.append(

            event.to_dict()

        )


        return {

            "listener": self.name,

            "event_received": event.event_type,

            "received_at": datetime.now().isoformat()

        }



    def history(self):

        return self.received_events