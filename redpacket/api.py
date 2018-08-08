from flask import Flask
from flask import jsonify
from flask import request
from excep import Excep
from models import send_redpacket
from models import grab_redpacket
from cache import is_exists

app = Flask(__name__)




@app.errorhandler(Excep)
def excep_handler(error):
    return jsonify({"status": error.status_code, "error":error.message})



@app.route("/api/v1/send", methods=['POST'])
def api_v1_send():
    # TODO GET UID BY Token
    
    # check personal balance
    d = request.get_json()
    uid = d.get("uid")
    amount = d.get("amount")
    number = d.get("number")
    f_type = d.get("type") or 1
    f_min = d.get("min") or 0.05

    # random generate put it all into the redis queue & set expire time
    key = send_redpacket(uid, amount, number, f_type, f_min)
    return jsonify({"key": key})


@app.route("/api/v1/grab", methods=['POST'])
def api_v1_grab():
    # TODO GET UID BY Token
    
    # check cache if the redpackaet exists or expire
    d = request.get_json()
    key = d.get("key") or ''
    uid = d.get("uid")
    if not is_exists(key):
        raise Excep("Invalid redpacket", 412)
    coin = grab_redpacket(key, uid)

    return jsonify({"coin": coin})



if __name__ == '__main__':
    app.run(debug=True)



