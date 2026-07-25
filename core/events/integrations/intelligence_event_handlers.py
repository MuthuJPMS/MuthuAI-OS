from datetime import datetime

from core.events.event_bus import event_bus

from core.memory.intelligence.memory_graph_bridge import memory_graph_bridge



class IntelligenceEventHandlers:


    def __init__(self):

        self.memory_bridge = memory_graph_bridge



    def handle_mission_completed(self, event):


        data = event.data


        task = data.get(
            "task",
            "Unknown Mission"
        )


        agent = data.get(
            "agent",
            "Unknown Agent"
        )


        result = data.get(
            "result",
            "Completed"
        )


        knowledge = self.memory_bridge.save_intelligent_memory(

            task,

            agent,

            result

        )


        return {

            "event": event.event_type,

            "knowledge_updated": True,

            "result": knowledge,

            "time": datetime.now().isoformat()

        }



    def handle_agent_completed(self, event):


        return {

            "event": event.event_type,

            "agent": event.source,

            "status": "processed",

            "time": datetime.now().isoformat()

        }



    def register_handlers(self):


        event_bus.subscribe(

            "mission_completed",

            self.handle_mission_completed

        )


        event_bus.subscribe(

            "agent_completed",

            self.handle_agent_completed

        )


        return {

            "status": "handlers_registered"

        }



intelligence_event_handlers = IntelligenceEventHandlers()