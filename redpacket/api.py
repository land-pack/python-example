from flask import Flask
from flask import jsonify
from excep import Excep
from models import send_redpacket


app = Flask(__name__)




@app.errorhandler(Excep)
def excep_handler(error):
    return jsonify({"status": error.status_code, "error":error.message})



@app.route("/api/v1/send")
def api_v1_send():
    # check personal balance

    # amount suggestion

    # random generate put it all into the redis queue & set expire time
    #return jsonify({"status":"ok"})
    send_redpacket(12345, 11, 12, 1)
    

    #raise Excep('No privilege to ...', 401)

    return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)



