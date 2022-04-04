from flask import Flask, render_template

LogSign = Flask(__name__)

@LogSign.route("/")
def login():
    return render_template("login.html")

@LogSign.route("/register")
def register():
    return render_template("signup.html")

if __name__ == "__main__":
    LogSign.run()
