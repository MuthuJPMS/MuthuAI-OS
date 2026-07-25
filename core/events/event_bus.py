from datetime import datetime

from core.events.event import Event



class EventBus:


    def __init__(self):

        self.listeners = {}

        self.event_history = []



    def subscribe(self, event_type, listener):

        if event_type not in self.listeners:

            self.listeners[event_type] = []


        self.listeners[event_type].append(listener)


        return {

            "status": "subscribed",

            "event": event_type

        }



    def publish(
        self,
        event_type,
        source,
        data=None
    ):


        event = Event(

            event_type,

            source,

            data

        )


        self.event_history.append(

            event.to_dict()

        )


        if event_type in self.listeners:

            for listener in self.listeners[event_type]:

                listener(event)



        return {

            "status": "published",

            "event": event.to_dict(),

            "time": datetime.now().isoformat()

        }



    def get_history(self):

        return self.event_history



event_bus = EventBus()