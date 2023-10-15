from flask import Flask
from clientApp_routes import path

clientApp = Flask(__name__)
clientApp.register_blueprint('routes')


if (__name__) == '__main__':
    clientApp.run()