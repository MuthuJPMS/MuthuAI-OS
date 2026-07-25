from datetime import datetime

from core.knowledge.knowledge_graph import knowledge_graph



class RelationshipManager:


    def __init__(self):

        self.graph = knowledge_graph



    def create_relationship(
        self,
        source_id,
        target_id,
        relationship
    ):


        result = self.graph.connect_nodes(

            source_id,

            target_id,

            relationship

        )


        result["created_at"] = datetime.now().isoformat()


        return result



    def find_relationships(self, node_id):


        node = self.graph.nodes.get(node_id)


        if node:

            return node.connections


        return []



    def understand_entity(self, keyword):


        nodes = self.graph.search(keyword)


        return {

            "keyword": keyword,

            "related_entities": nodes,

            "analyzed_at": datetime.now().isoformat()

        }



relationship_manager = RelationshipManager()