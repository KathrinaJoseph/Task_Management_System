from flask import Blueprint, request, jsonify
from service.task_manager import TaskManager
from util.exceptions import TaskManagerException

user_bp = Blueprint("user", __name__)
tm = TaskManager()

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    required_fields = ["user_id", "name", "email"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400
    
    try:
        tm.create_user(data["user_id"], data["name"], data["email"])
        return jsonify({"message": "User created successfully"}), 201
    except TaskManagerException as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

@user_bp.route("/", methods=["GET"])
def list_users():
    try:
        # Instead of just printing, return the data
        users = tm.list_all_users()  # Assuming this returns user data
        return jsonify({"users": users}), 200
    except Exception as e:
        return jsonify({"error": "Failed to retrieve users"}), 500