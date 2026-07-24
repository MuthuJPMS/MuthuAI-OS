class PermissionManager:


    def __init__(self):

        self.rules = {

            "money_transfer": False,
            "data_delete": False,
            "publish_content": False

        }


    def check(self, action):

        return self.rules.get(action, False)


    def request_permission(self, action):

        return {
            "action": action,
            "required": True,
            "status": "waiting_for_approval"
        }



permission_manager = PermissionManager()