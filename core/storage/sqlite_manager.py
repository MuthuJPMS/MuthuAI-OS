from core.storage.database import get_connection


class SQLiteManager:


    def save_agent(self, name, role):

        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO agents(name,role)
            VALUES (?,?)
            """,
            (name, role)
        )

        db.commit()
        db.close()


    def save_memory(self, memory, memory_type):

        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO memories(memory,memory_type)
            VALUES (?,?)
            """,
            (memory, memory_type)
        )

        db.commit()
        db.close()


    def get_memories(self):

        db = get_connection()
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM memories"
        )

        data = cursor.fetchall()

        db.close()

        return [dict(row) for row in data]



sqlite_manager = SQLiteManager()