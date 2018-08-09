from flask import jsonify
from flask import request
from flask import Blueprint
from flask_cors import CORS
from project.core.excep import Excep
from project.models import send_redpacket
from project.models import grab_redpacket
from project.utils.cache import is_exists
from project.utils.log import logger


# Config

redpacket_blueprint = Blueprint('redpacket', __name__, template_folder='templates')

CORS(redpacket_blueprint)







@redpacket_blueprint.errorhandler(Excep)
def excep_handler(error):
    return jsonify({"status": error.status_code, "error":error.message})



@redpacket_blueprint.route("/api/v1/send", methods=['POST'])
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


@redpacket_blueprint.route("/api/v1/grab", methods=['POST'])
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
    logger.info(">>>>>>>>>>>>>Fire <<<<")
    app.run(debug=True)



