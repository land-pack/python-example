from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/api/v1/send")
def api_v1_send():
    # check personal balance

    # amount suggestion

    # random generate put it all into the redis queue & set expire time
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(debug=True)



