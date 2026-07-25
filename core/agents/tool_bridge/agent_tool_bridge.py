from datetime import datetime

from core.tools.tool_registry import tool_registry



class AgentToolBridge:


    def __init__(self):

        self.registry = tool_registry



    def discover_tools(self):

        return self.registry.list_tools()



    def execute_capability(self, tool_name, **parameters):


        result = self.registry.execute_tool(

            tool_name,

            **parameters

        )


        return {

            "agent_tool_bridge": True,

            "tool": tool_name,

            "result": result,

            "executed_at": datetime.now().isoformat()

        }



    def check_tool_available(self, tool_name):


        tool = self.registry.get_tool(tool_name)


        return {

            "tool": tool_name,

            "available": tool is not None

        }



agent_tool_bridge = AgentToolBridge()