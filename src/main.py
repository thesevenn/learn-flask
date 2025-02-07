from flask import Flask, request, jsonify, redirect, render_template, session
from routes.user.route import user
app = Flask(__name__)

app.secret_key = "random_secret_key"
app.register_blueprint(blueprint=user, url_prefix="/user")


@app.route("/",  methods=["GET", "POST"])
def handler():
    if request.method == "POST":
        return post()
    else:
        return jsonify({"name": "George"})


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard_handler():
    if request.method == "GET":
        try:
            username = session["user"]
            upass = session["pass"]
            if not username or not upass:
                return redirect("/login")
            else:
                return render_template("dashboard.html", username=username)
        except KeyError as ky:
            return redirect("/login")


def post():
    name = request.form["name"]
    upass = request.form["pass"]
    return jsonify({"name": name, "pass": upass}), 201


@app.route("/user/<int:_id>", methods=["GET"])
def user_handler(_id):
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


@app.route("/login", methods=["POST","GET"])
def login_handler():
    if request.method == "POST":
        name = request.form["username"]
        upass = request.form["password"]
        if not name or not upass:
            return f"Invalid input, try again"

        session["user"] = name
        session["pass"] = upass
        return redirect("/dashboard")
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET"])
def logout_handler():
    try:
        session.pop("user")
        session.pop("pass")
        return redirect("/login")
    except KeyError as ky:
        print(f"Error: {ky}")
        return redirect("/dashboard")


@app.route("/jinja", methods=["GET"])
def handle_template():
    return render_template("example.html",
                           test=True,
                           task="Today tasks",
                           tasks=["Good work", "Other work", "More work", "Another task"])


if __name__ == "__main__":
    app.run(debug=True)
