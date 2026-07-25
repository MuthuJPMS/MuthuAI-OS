from core.knowledge.knowledge_node import KnowledgeNode



class KnowledgeGraph:


    def __init__(self):

        self.nodes = {}



    def create_node(self, name, node_type, metadata=None):

        node = KnowledgeNode(

            name,

            node_type,

            metadata

        )

        self.nodes[node.id] = node


        return node.to_dict()



    def get_node(self, node_id):

        node = self.nodes.get(node_id)


        if node:

            return node.to_dict()


        return None



    def connect_nodes(self, source_id, target_id, relationship):


        source = self.nodes.get(source_id)


        if source:

            source.add_connection(

                target_id,

                relationship

            )


            return {

                "status": "connected",

                "from": source_id,

                "to": target_id,

                "relationship": relationship

            }


        return {

            "status": "error",

            "message": "Source node not found"

        }



    def search(self, keyword):

        results = []


        keyword = keyword.lower()


        for node in self.nodes.values():

            if keyword in node.name.lower():

                results.append(

                    node.to_dict()

                )


        return results



    def list_nodes(self):

        return [

            node.to_dict()

            for node in self.nodes.values()

        ]



knowledge_graph = KnowledgeGraph()