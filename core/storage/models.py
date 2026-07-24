class AgentModel:

    def __init__(self, name, role):
        self.name = name
        self.role = role



class TaskModel:

    def __init__(self, task, agent, status):
        self.task = task
        self.agent = agent
        self.status = status



class MemoryModel:

    def __init__(self, memory, memory_type):
        self.memory = memory
        self.memory_type = memory_type