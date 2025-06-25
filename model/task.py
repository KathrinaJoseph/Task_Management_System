class Task:
    """Represents a task with details and assignment status.

   """
    def __init__(self, task_id, title, description, due_date, priority="Low"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = None
        self.status = "To Do"
        self.priority = priority
        self.due_date = due_date

    def update_status(self, new_status):
        """Update the task's status to a new value.

        Args:
            new_status (str): New status like "In Progress" or "Done".
        """
        self.status = new_status

    def update_priority(self, new_priority):
        """Change the task's priority level.

        Args:
            new_priority (str): New priority level such as "High".
        """
        self.priority = new_priority

    def assign_to(self, user):
        """Assign the task to a specific user.

        Args:
            user (User): The user to assign the task to.
        """
        self.assigned_to = user

    def __str__(self):
        """
        Print the task details in a formatted way.
        """
        assigned = self.assigned_to.name if self.assigned_to else "None"
        print(f"Task[{self.task_id}]: {self.title} | Status: {self.status} | Priority: {self.priority} | Due: {self.due_date}| Assigned to: {assigned}")
