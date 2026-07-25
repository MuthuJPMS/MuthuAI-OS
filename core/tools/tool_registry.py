from datetime import datetime


class ToolRegistry:


    def __init__(self):

        self.tools = {}



    def register(self, tool):

        self.tools[tool.name] = tool

        return {

            "status": "registered",

            "tool": tool.name,

            "registered_at": datetime.now().isoformat()

        }



    def get_tool(self, name):

        return self.tools.get(name)



    def list_tools(self):

        return [

            {

                "name": tool.name,

                "description": tool.description

            }

            for tool in self.tools.values()

        ]



    def execute_tool(self, name, **kwargs):

        tool = self.get_tool(name)


        if tool is None:

            return {

                "status": "error",

                "message": f"Tool {name} not found"

            }


        result = tool.execute(**kwargs)


        return {

            "status": "success",

            "tool": name,

            "result": result

        }



tool_registry = ToolRegistry()