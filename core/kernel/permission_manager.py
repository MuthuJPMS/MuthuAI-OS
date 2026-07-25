from datetime import datetime
import uuid


from core.infrastructure.logger import logger
from core.infrastructure.health_monitor import health_monitor



class PermissionManager:


    def __init__(self):

        self.permissions = {}

        self.approval_requests = {}

        self.audit_logs = []


        health_monitor.register_component(
            "Permission Manager"
        )


        logger.info(
            "Permission Manager initialized"
        )



    def register_identity(

        self,

        identity,

        role="user"

    ):


        self.permissions[identity] = {


            "role": role,

            "permissions": [],

            "created_at":
                datetime.now().isoformat()

        }


        return self.permissions[identity]



    def grant_permission(

        self,

        identity,

        permission

    ):


        if identity not in self.permissions:

            self.register_identity(identity)


        self.permissions[identity]["permissions"].append(

            permission

        )


        logger.info(

            f"Permission granted: {identity} -> {permission}"

        )


        return {

            "status": "granted",

            "identity": identity,

            "permission": permission

        }



    def check_permission(

        self,

        identity,

        action

    ):


        user = self.permissions.get(identity)


        if not user:

            return False


        return action in user["permissions"]



    def request_approval(

        self,

        identity,

        action,

        reason

    ):


        request_id = str(uuid.uuid4())


        request = {


            "id": request_id,

            "identity": identity,

            "action": action,

            "reason": reason,

            "status": "waiting",

            "created_at":
                datetime.now().isoformat()

        }


        self.approval_requests[request_id] = request


        self.audit(

            "approval_requested",

            request

        )


        return request



    def approve(

        self,

        request_id

    ):


        if request_id not in self.approval_requests:

            return None


        self.approval_requests[request_id]["status"] = "approved"


        self.audit(

            "approval_granted",

            self.approval_requests[request_id]

        )


        return self.approval_requests[request_id]



    def reject(

        self,

        request_id

    ):


        if request_id not in self.approval_requests:

            return None


        self.approval_requests[request_id]["status"] = "rejected"


        self.audit(

            "approval_rejected",

            self.approval_requests[request_id]

        )


        return self.approval_requests[request_id]



    def audit(

        self,

        event,

        data

    ):


        self.audit_logs.append(

            {

                "event": event,

                "data": data,

                "time":
                    datetime.now().isoformat()

            }

        )



    def get_audit_logs(self):

        return self.audit_logs



permission_manager = PermissionManager()