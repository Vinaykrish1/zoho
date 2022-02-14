from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hi():
    return render_template("sign_in.html")


@app.route("/sign_in.html")
def hi_0():
    return render_template("sign_in.html")


@app.route("/sign_up.html")
def hi_1():
    return render_template("sign_up.html")


@app.route("/forgot.html")
def hi_2():
    return render_template("forgot.html")


@app.route("/comment.html")
def hi_3():
    return render_template("comment.html")


if __name__ == "__main__":
    app.run(debug=True)
