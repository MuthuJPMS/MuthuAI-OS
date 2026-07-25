from core.tools.base_tool import BaseTool



class TestTool(BaseTool):


    def __init__(self):

        super().__init__(

            "test_tool",

            "Basic testing tool for MuthuAI Tool Registry"

        )



    def execute(self, message="Hello MuthuAI"):

        return {

            "message": message,

            "result": "Tool execution successful"

        }



test_tool = TestTool()