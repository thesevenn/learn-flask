from flask import Flask, request, jsonify, redirect, render_template
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


@app.route("/hello/<name>", methods=["GET"])
def hello_handler(name):
    if name == "mike":
        return redirect("/")
    return (f"<h1 style='font-weight:400;font-size:60px;color:turquoise;font-family:sans-serif;'>"
            f"Hello {name}, What you are up to?</h1>")


@app.route("/process", methods=["POST", "GET"])
def handle_form():
    if request.method == "GET":
        return render_template("form.html", form="User Details")
    name = request.form["name"]
    pws = request.form["pass"]
    if not name or not pws:
        return "Cannot be empty!!"
    else:
        return f"Thank you for your input, {name}, with password: {pws}"


@app.route("/login", methods=["POST"])
def login_handler():
    name = request.form["name"]
    upass = request.form["pass"]
    if name == "andrew" and upass == "xj3j94;1":
        return jsonify({"status": "success", "user": "andrew", "message": "Welcome back!, login success"})
    else:
        return jsonify({"status": "failure", "user": "Not found", "message": "Login Failed!!, Invalid credentials"})


@app.route("/jinja", methods=["GET"])
def handle_template():
    return render_template("example.html",
                           test=True,
                           task="Today tasks",
                           tasks=["Good work", "Other work", "More work", "Another task"])


if __name__ == "__main__":
    app.run(debug=True)
