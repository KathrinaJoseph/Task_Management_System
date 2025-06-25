from flask import Blueprint, request, jsonify
from service.task_manager import TaskManager
from util.exceptions import TaskManagerException

task_bp = Blueprint("task", __name__)
tm = TaskManager()

@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    required_fields = ["task_id", "title", "description", "due_date"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400
    
    try:
        tm.create_task(data["task_id"], data["title"], data["description"],
                       data["due_date"], data.get("priority", "Low"))
        return jsonify({"message": "Task created successfully"}), 201
    except TaskManagerException as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@task_bp.route("/", methods=["GET"])
def list_tasks():
    try:
        # Return actual data instead of console message
        tasks = tm.list_all_tasks()  # Assuming this returns task data
        return jsonify({"tasks": tasks}), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve tasks"}), 500

@task_bp.route("/assign", methods=["PUT"])
def assign_task():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    required_fields = ["task_id", "user_id"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400
    
    try:
        tm.assign_task_to_user(data["task_id"], data["user_id"])
        return jsonify({"message": "Task assigned successfully"}), 200
    except TaskManagerException as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@task_bp.route("/user/<user_id>", methods=["GET"])
def tasks_by_user(user_id):
    try:
        # Return actual data instead of console message
        tasks = tm.list_tasks_by_user(user_id)  # Assuming this returns task data
        return jsonify({"user_id": user_id, "tasks": tasks}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve tasks for user {user_id}"}), 500

@task_bp.route("/status/<status>", methods=["GET"])
def tasks_by_status(status):
    try:
        # Return actual data instead of console message
        tasks = tm.list_tasks_by_status(status)  # Assuming this returns task data
        return jsonify({"status": status, "tasks": tasks}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to retrieve tasks with status '{status}'"}), 500