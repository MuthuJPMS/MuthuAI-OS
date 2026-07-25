from datetime import datetime
import uuid



class Event:


    def __init__(
        self,
        event_type,
        source,
        data=None
    ):

        self.id = str(uuid.uuid4())

        self.event_type = event_type

        self.source = source

        self.data = data or {}

        self.created_at = datetime.now().isoformat()



    def to_dict(self):

        return {

            "id": self.id,

            "event_type": self.event_type,

            "source": self.source,

            "data": self.data,

            "created_at": self.created_at

        }