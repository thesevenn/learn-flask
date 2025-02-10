from flask import Blueprint, request

user = Blueprint("user", __name__)

users = list()


@user.route("/", methods=["GET"])
def index():
    return "Main user route"


@user.route("/new", methods=["POST"])
def new_handler():
    try:
        name = request.form["name"]
        age = request.form["age"]
        _id = request.form["id"]
        users.append({name: name, age: age, id: _id})
        return f"Hello, {name}, {age}"
    except KeyError as ky:
        print(f"Error: {ky}")
        return "Something went wrong"


@user.route("/remove/<int:_id>", methods=["DELETE"])
def remove_user(_id):
    try:
        global users
        users = [_user for _user in users if _user.id == _id]
        return f"User with id: {_id} removed successfully"
    except ValueError as e:
        print(f"Error: {e}")
        return f"User not found with {_id}"


@user.route("/*", methods=["GET", "POST", "DELETE", "PUT", "UPDATE"])
def error_handler():
    return "Error: Not found", 404
