import uuid
from flask import Flask, render_template, make_response, request, redirect
import redis

app = Flask(__name__)


r = redis.Redis(host="127.0.0.1", port=6379)


@app.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    username = request.form.get('username', 'root')
    password= request.form.get('password', 'root')
    print("username={} || password={}".format(username, password))
    if request.method == "POST":
        if username == 'admin' and password == 'admin':
            res = make_response(redirect('/vips'))
            expires_time = 60 * 60 * 24 
            person_info = "skanfanfl aksndkansd aks dksabd aksndas"
            token_key = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
            res.set_cookie("token", token_key)
            r.set(token_key, person_info, expires_time)
            return res
        else:
            return render_template("auth/login.html")

    else:
        return render_template("auth/login.html")



@app.route("/auth/signup")
def signup():
    #return render_template("signup.html")
    return render_template("auth/signup.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitl 
    return render_template('error/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
