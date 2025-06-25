from util.exceptions import ValidationError

def validate_user_id(user_id):
    """
    Validates that the user ID is a non-empty string.

    Args:
        user_id (str): The user ID to validate.

    Raises:
        ValidationError: If the user ID is empty or not a string.
    """
    if not user_id or not isinstance(user_id, str):
        raise ValidationError("User ID must be a non-empty string.", field="user_id", value=user_id)


def validate_email(email):
    """
    Validates that the email contains an '@' symbol.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email is empty or does not contain an '@'.
    """
    if not email or "@" not in email:
        raise ValidationError("Invalid email format.", field="email", value=email)


def validate_task_id(task_id):
    """
    Validates that the task ID is a string starting with 'T-'.

    Args:
        task_id (str): The task ID to validate.

    Raises:
        ValidationError: If the task ID is empty or does not start with 'T-'.
    """
    if not task_id or not task_id.startswith("T-"):
        raise ValidationError("Task ID must start with 'T-'.", field="task_id", value=task_id)


def validate_priority(priority):
    """
    Validates that the priority is one of the allowed values: Low, Medium, or High.

    Args:
        priority (str): The priority level to validate (case insensitive).

    Raises:
        ValidationError: If the priority is not one of the allowed values.
    """
    valid = ['low', 'medium', 'high']
    if priority.lower() not in valid:
        raise ValidationError("Priority must be Low, Medium, or High.", field="priority", value=priority)


def validate_status(status):
    """
    Validates that the task status is one of the allowed statuses.

    Args:
        status (str): The status to validate. Must be exactly: 'To Do', 'In Progress', or 'Done'.

    Raises:
        ValidationError: If the status is not one of the exact allowed values.
    """
    valid = ['To Do', 'In Progress', 'Done']
    if status not in valid:
        raise ValidationError("Status must be 'To Do', 'In Progress', or 'Done'.", field="status", value=status)


def validate_due_date(date_str):
    """
    Validates that the due date string is in 'YYYY-MM-DD' format.

    Args:
        date_str (str): The due date to validate.

    Raises:
        ValidationError: If the date format is invalid or not properly structured.
    """
    if not date_str or len(date_str.split("-")) != 3:
        raise ValidationError("Due date must be in YYYY-MM-DD format.", field="due_date", value=date_str)
