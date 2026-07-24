from datetime import datetime


class DepartmentManager:


    def __init__(self):

        self.departments = []


    def create_department(
        self,
        name,
        responsibility,
        agents
    ):

        department = {

            "department": name,

            "responsibility": responsibility,

            "agents": agents,

            "created_at": datetime.now().isoformat(),

            "status": "active"

        }


        self.departments.append(
            department
        )

        return department



    def list_departments(self):

        return self.departments



department_manager = DepartmentManager()