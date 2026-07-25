from datetime import datetime
import uuid


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor



class SecurityCenter:


    def __init__(self):

        self.security_events = []

        self.active_sessions = {}

        self.blocked_actions = []

        health_monitor.register_component(
            "Security Center"
        )

        logger.info(
            "Security Center initialized"
        )



    def create_session(

        self,

        identity,

        role="user"

    ):


        session_id = str(uuid.uuid4())


        session = {

            "session_id": session_id,

            "identity": identity,

            "role": role,

            "created_at":
                datetime.now().isoformat(),

            "status": "active"

        }


        self.active_sessions[session_id] = session


        self.record_event(

            "session_created",

            session

        )


        return session



    def validate_session(

        self,

        session_id

    ):


        session = self.active_sessions.get(
            session_id
        )


        if not session:

            return False


        return session["status"] == "active"



    def block_action(

        self,

        identity,

        action,

        reason

    ):


        event = {


            "identity": identity,

            "action": action,

            "reason": reason,

            "blocked_at":
                datetime.now().isoformat()

        }


        self.blocked_actions.append(event)


        self.record_event(

            "action_blocked",

            event

        )


        logger.warning(

            f"Blocked action: {action}"

        )


        return event



    def record_event(

        self,

        event_type,

        data

    ):


        event = {

            "id": str(uuid.uuid4()),

            "type": event_type,

            "data": data,

            "time":
                datetime.now().isoformat()

        }


        self.security_events.append(event)


        return event



    def security_status(self):


        health_monitor.update_status(

            "Security Center",

            "healthy",

            "Security monitoring active"

        )


        return {

            "status": "active",

            "sessions":
                len(self.active_sessions),

            "events":
                len(self.security_events),

            "blocked_actions":
                len(self.blocked_actions)

        }



security_center = SecurityCenter()