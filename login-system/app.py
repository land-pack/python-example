from flask import Flask, render_template


app = Flask(__name__)


@app.route("/auth/login")
def login():
    return render_template("login.html")



@app.route("/auth/signup")
def signup():
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
