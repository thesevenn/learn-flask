from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/",  methods=["GET", "POST"])
def handler():
    if request.method == "POST":
        return post()
    else:
        return jsonify({"name": "George"})


def post():
    name = request.form["name"]
    upass = request.form["pass"]
    return jsonify({"name": name, "pass": upass}), 201


@app.route("/user/<int:_id>", methods=["GET"])
def user_handler(_id):
    if request.method == "POST":
        return jsonify({"error": "Method not Allowed"}), 405
    else:
        return jsonify({"message": f"Your data is found at x1dfa_{_id}"})


@app.route("/login", methods=["POST"])
def login_handler():
    name = request.form["name"]
    upass = request.form["pass"]
    if name == "andrew" and upass == "xj3j94;1":
        return jsonify({"status": "success", "user": "andrew", "message": "Welcome back!, login success"})
    else:
        return jsonify({"status": "failure", "user": "Not found", "message": "Login Failed!!, Invalid credentials"})


if __name__ == "__main__":
    app.run()
