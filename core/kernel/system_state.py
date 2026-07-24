from datetime import datetime


class SystemState:

    def __init__(self):
        self.status = "online"
        self.mode = "development"
        self.active_tasks = 0
        self.active_agents = []
        self.started_at = datetime.now().isoformat()


    def update_status(self, status):
        self.status = status


    def add_agent(self, agent_name):
        if agent_name not in self.active_agents:
            self.active_agents.append(agent_name)


    def add_task(self):
        self.active_tasks += 1


    def complete_task(self):
        if self.active_tasks > 0:
            self.active_tasks -= 1


    def get_state(self):

        return {
            "status": self.status,
            "mode": self.mode,
            "active_tasks": self.active_tasks,
            "active_agents": self.active_agents,
            "started_at": self.started_at
        }


system_state = SystemState()