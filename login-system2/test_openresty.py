from flask import Flask
from flask import jsonify
from flask import make_response
import redis


app = Flask(__name__)
r = redis.Redis(host="127.0.0.1", port=6379)

@app.route("/index")
def index():
    return jsonify({"key": "index"})

@app.route("/vip/a")
def vip_a():
    return jsonify({"key": "a"})


@app.route("/vip/b")
def vip_b():
    return jsonify({"key": "a"})


@app.route("/hello")
def hello():
    return jsonify({"key": "a"})

@app.route("/account/login/<item_name>/<token_key>")
def login(item_name, token_key):
    expires_time = 60 * 60 * 24 
    person_info = "skanfanfl aksndkansd aks dksabd aksndas"
    res = make_response(jsonify({"key": "login"}))
    #res.set_cookie(item_name, token_key, expires=expires_time)
    res.set_cookie(item_name, token_key)
    r.set(token_key, person_info, expires_time)
    return res


if __name__ == '__main__':
    app.run(debug=True)
