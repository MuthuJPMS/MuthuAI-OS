from datetime import datetime

from core.knowledge.knowledge_graph import knowledge_graph

from core.memory.v2.memory_bridge import memory_bridge



class MemoryGraphBridge:


    def __init__(self):

        self.memory = memory_bridge

        self.graph = knowledge_graph



    def convert_memory_to_knowledge(
        self,
        task,
        agent,
        result
    ):


        # Create main execution node

        execution_node = self.graph.create_node(

            task,

            "Execution",

            {

                "agent": agent,

                "result": result

            }

        )


        # Create agent node

        agent_node = self.graph.create_node(

            agent,

            "AI Agent",

            {

                "active": True

            }

        )


        # Connect relationship

        self.graph.connect_nodes(

            agent_node["id"],

            execution_node["id"],

            "performed"

        )


        return {


            "status": "knowledge_created",

            "execution": execution_node,

            "agent": agent_node,

            "created_at": datetime.now().isoformat()

        }



    def save_intelligent_memory(
        self,
        task,
        agent,
        result
    ):


        # Save normal memory

        memory_result = self.memory.save_execution(

            task,

            agent,

            result

        )


        # Convert into knowledge

        knowledge_result = self.convert_memory_to_knowledge(

            task,

            agent,

            result

        )


        return {


            "memory": memory_result,

            "knowledge": knowledge_result

        }



memory_graph_bridge = MemoryGraphBridge()