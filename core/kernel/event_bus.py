from datetime import datetime


class EventBus:

    def __init__(self):
        self.events = []


    def publish(self, event_name, data):

        event = {
            "event": event_name,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

        self.events.append(event)

        return event


    def get_events(self):

        return self.events



event_bus = EventBus()