"""
MuthuAI OS - Tool Manager v1

Responsible for:
- Registering tools
- Managing agent tools
- Executing tools
"""


from datetime import datetime



class ToolManager:


    def __init__(self):

        self.tools = {}



    def register_tool(self, name, function, description=""):

        self.tools[name] = {

            "function": function,

            "description": description,

            "created_at": datetime.now().isoformat()

        }


        return {

            "tool": name,

            "status": "registered"

        }




    def list_tools(self):

        return list(self.tools.keys())




    def execute(self, tool_name, *args, **kwargs):

        if tool_name not in self.tools:

            return {

                "error": "Tool not found"

            }


        tool = self.tools[tool_name]["function"]


        result = tool(*args, **kwargs)


        return {

            "tool": tool_name,

            "result": result,

            "executed_at": datetime.now().isoformat()

        }



tool_manager = ToolManager()