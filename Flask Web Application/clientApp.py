from flask import Flask
from clientApp_routes import path

clientApp = Flask(__name__)
clientApp.register_blueprint(path)


if (__name__) == '__main__':
    clientApp.run(debug=True)