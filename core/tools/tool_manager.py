from datetime import datetime

from core.tools.tool_registry import tool_registry



class ToolManager:


    def __init__(self):

        self.registry = tool_registry

        self.disabled_tools = []



    def install_tool(self, tool):

        result = self.registry.register(tool)


        return {

            "action": "install",

            "result": result

        }



    def enable_tool(self, tool_name):

        if tool_name in self.disabled_tools:

            self.disabled_tools.remove(tool_name)


        return {

            "tool": tool_name,

            "status": "enabled",

            "time": datetime.now().isoformat()

        }



    def disable_tool(self, tool_name):

        if tool_name not in self.disabled_tools:

            self.disabled_tools.append(tool_name)


        return {

            "tool": tool_name,

            "status": "disabled",

            "time": datetime.now().isoformat()

        }



    def available_tools(self):

        tools = self.registry.list_tools()


        return [

            tool

            for tool in tools

            if tool["name"] not in self.disabled_tools

        ]



    def tool_status(self):

        return {

            "total_tools": len(self.registry.tools),

            "disabled_tools": self.disabled_tools,

            "checked_at": datetime.now().isoformat()

        }



tool_manager = ToolManager()