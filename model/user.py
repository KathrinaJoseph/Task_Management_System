
class User:
    """Represents a user in the task management system.
    """
    def __init__(self, user_id, name, email):

        """
        Initialize a User with ID, name, email and task list.
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.task_list = []

    def add_task(self, task):
        """
        Add a task to the user's task list.
        """
        self.task_list.append(task)

    def remove_task(self, task_id):
        """
        Remove a task from the user's task list by task ID.
        """
        self.task_list = [task for task in self.task_list if task.task_id != task_id]

    def view_tasks_by_status(self, status):
        """
        Return tasks that match a specific status.
        """
        return [task for task in self.task_list if task.status == status]

