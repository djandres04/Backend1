from flask import Flask, request, jsonify
from flask_cors import CORS

# config
from config import config

# routes
from routes import HomeRoute
from routes import DevicesRoute
from routes import DoorRoute, LightRoute

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(HomeRoute.main, url_prefix='/')
    app.register_blueprint(DevicesRoute.main, url_prefix='/devices')
    app.register_blueprint(DoorRoute.main, url_prefix='/door')
    app.register_blueprint(LightRoute.main, url_prefix='/light')

    app.run(host="0.0.0.0", port=5050, debug=True)
