from flask import Flask
from controllers.user_controller import user_bp
from controllers.task_controller import task_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(task_bp, url_prefix="/tasks")

# Add a root route to handle base URL
@app.route("/")
def home():
    return {
        "message": "Task Manager API",
        "endpoints": {
            "users": "/users",
            "tasks": "/tasks"
        }
    }, 200

# Add error handler for 404
@app.errorhandler(404)
def not_found(error):
    return {
        "error": "Not Found",
        "message": "The requested URL was not found on the server.",
        "available_endpoints": {
            "GET /": "API information",
            "POST /users/": "Create user",
            "GET /users/": "List users",
            "POST /tasks/": "Create task",
            "GET /tasks/": "List tasks",
            "PUT /tasks/assign": "Assign task",
            "GET /tasks/user/<user_id>": "Get user tasks",
            "GET /tasks/status/<status>": "Get tasks by status"
        }
    }, 404

if __name__ == "__main__":
    app.run(debug=True)
