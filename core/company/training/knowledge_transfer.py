from datetime import datetime


class KnowledgeTransfer:


    def __init__(self):

        self.transfers = []



    def transfer(
        self,
        from_agent,
        to_agent,
        knowledge
    ):

        data = {

            "source": from_agent,

            "receiver": to_agent,

            "knowledge": knowledge,

            "transferred_at": datetime.now().isoformat()

        }


        self.transfers.append(data)

        return data



    def list_transfers(self):

        return self.transfers



knowledge_transfer = KnowledgeTransfer()