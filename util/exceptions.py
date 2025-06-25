class TaskManagerException(Exception):
    """
    Base exception for the Task Management System.
    All custom exceptions should inherit from this.
    """
    pass


class InvalidInputError(TaskManagerException):
    """
    Raised when user input cannot be parsed (e.g., converting string to int).

    Args:
        message (str): Description of the error. Defaults to "Invalid input provided."
        original_exception (Exception, optional): The original exception that caused this error, such as ValueError.
    """
    def __init__(self, message="Invalid input provided.", original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception


class ValidationError(TaskManagerException):
    """
    Raised when input fails custom validation rules.

    Args:
        message (str): Description of the error. Defaults to "Validation failed."
        field (str, optional): The name of the field that failed validation.
        value (any, optional): The invalid value provided.
    """
    def __init__(self, message="Validation failed.", field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value


class DuplicateUserException(TaskManagerException):
    """
    Raised when trying to create a user that already exists.

    Args:
        message (str): Description of the error. Defaults to "User already exists."
        user_id (str, optional): The user ID that caused the duplication error.
    """
    def __init__(self, message="User already exists.", user_id=None):
        super().__init__(message)
        self.user_id = user_id


class DuplicateTaskException(TaskManagerException):
    """
    Raised when trying to create a task with an ID that already exists.

    Args:
        message (str): Description of the error. Defaults to "Task ID already exists."
        task_id (str, optional): The task ID that caused the duplication error.
    """
    def __init__(self, message="Task ID already exists.", task_id=None):
        super().__init__(message)
        self.task_id = task_id


class NotFoundException(TaskManagerException):
    """
    Raised when a requested item (task or user) is not found.

    Args:
        message (str): Description of the error. Defaults to "Item not found."
        item_id (str, optional): The ID of the missing item (task or user).
    """
    def __init__(self, message="Item not found.", item_id=None):
        super().__init__(message)
        self.item_id = item_id
