import mysql.connector as connector  # ✅ Use alias 'connector'
from util.db import get_connection
from model.task import Task
from model.user import User
from util.exceptions import NotFoundException, DuplicateUserException, DuplicateTaskException


class TaskManager:
    def create_user(self, user_id, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO User (user_id, name, email) VALUES (%s, %s, %s)",
                (user_id, name, email)
            )
            conn.commit()
            print("User created.")
        except connector.IntegrityError:
            raise DuplicateUserException(user_id=user_id)
        finally:
            cursor.close()
            conn.close()

    def create_task(self, task_id, title, description, due_date, priority):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Task (task_id, title, description, due_date, priority)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (task_id, title, description, due_date, priority)
            )
            conn.commit()
            print("Task created.")
        except connector.IntegrityError:
            raise DuplicateTaskException(task_id=task_id)
        finally:
            cursor.close()
            conn.close()

    def assign_task_to_user(self, task_id, user_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT user_id FROM User WHERE user_id = %s", (user_id,))
            if not cursor.fetchone():
                raise NotFoundException("User not found.", item_id=user_id)

            cursor.execute("SELECT task_id FROM Task WHERE task_id = %s", (task_id,))
            if not cursor.fetchone():
                raise NotFoundException("Task not found.", item_id=task_id)

            cursor.execute(
                "UPDATE Task SET assigned_to = %s WHERE task_id = %s",
                (user_id, task_id)
            )
            conn.commit()
            print("Task assigned.")
        finally:
            cursor.close()
            conn.close()

    def list_all_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Task")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append(f"Task ID: {row[0]}, Title: {row[1]}, Status: {row[4]}, Priority: {row[5]}, Due: {row[6]}, Assigned to: {row[3]}")
        return tasks

    def list_tasks_by_user(self, user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Task WHERE assigned_to = %s", (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append(f"Task ID: {row[0]}, Title: {row[1]}, Status: {row[4]}, Priority: {row[5]}, Due: {row[6]}")
        return tasks

    def list_tasks_by_status(self, status):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Task WHERE status = %s", (status,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append(f"Task ID: {row[0]}, Title: {row[1]}, Assigned to: {row[3]}, Priority: {row[5]}, Due: {row[6]}")
        return tasks

    def list_all_users(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        users = []
        for row in rows:
            users.append(f"User ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
        return users
