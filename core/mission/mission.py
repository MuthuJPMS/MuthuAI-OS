from datetime import datetime
import uuid


class Mission:

    def __init__(self, title, category="General", priority=5):

        self.id = str(uuid.uuid4())

        self.title = title

        self.category = category

        self.priority = priority

        self.status = "created"

        self.created_at = datetime.now().isoformat()

        self.started_at = None

        self.completed_at = None

        self.progress = 0

        self.tasks = []

        self.assigned_agents = []


    def add_task(self, task):

        self.tasks.append(task)


    def assign_agent(self, agent):

        if agent not in self.assigned_agents:

            self.assigned_agents.append(agent)


    def start(self):

        self.status = "running"

        self.started_at = datetime.now().isoformat()


    def update_progress(self, progress):

        self.progress = progress

        if progress >= 100:

            self.complete()


    def complete(self):

        self.progress = 100

        self.status = "completed"

        self.completed_at = datetime.now().isoformat()


    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "category": self.category,

            "priority": self.priority,

            "status": self.status,

            "progress": self.progress,

            "tasks": self.tasks,

            "assigned_agents": self.assigned_agents,

            "created_at": self.created_at,

            "started_at": self.started_at,

            "completed_at": self.completed_at

        }