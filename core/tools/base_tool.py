from datetime import datetime


class BaseTool:


    def __init__(self, name, description):

        self.name = name

        self.description = description

        self.created_at = datetime.now().isoformat()



    def execute(self, **kwargs):

        raise NotImplementedError(
            "Tool must implement execute method"
        )



    def info(self):

        return {

            "name": self.name,

            "description": self.description,

            "created_at": self.created_at

        }