from datetime import datetime
import uuid


class KnowledgeNode:


    def __init__(self, name, node_type, metadata=None):

        self.id = str(uuid.uuid4())

        self.name = name

        self.node_type = node_type

        self.metadata = metadata or {}

        self.connections = []

        self.created_at = datetime.now().isoformat()



    def add_connection(self, node_id, relationship):

        self.connections.append(

            {

                "node_id": node_id,

                "relationship": relationship

            }

        )



    def update_metadata(self, key, value):

        self.metadata[key] = value



    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "type": self.node_type,

            "metadata": self.metadata,

            "connections": self.connections,

            "created_at": self.created_at

        }