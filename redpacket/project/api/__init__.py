from flask import Flask
from flask_cors import CORS





def create_app(config_name='base'):
    app = Flask(__name__, instance_relative_config=True)
    # cors = CORS(app, resources={r"/*": {"origins": "*"}})
    CORS(app, supports_credentials=True)
    
    from project.api.redpacket import redpacket_blueprint

    # register the blueprints
    app.register_blueprint(redpacket_blueprint)

    return app
