from flask import Flask                     # import Flask application
from medInfo import medInfo           # import Flask customized PyMongo from MongoDB
from clientApp_routes import path           # import the routes blueprint from clientApp_routes

clientApp = Flask(__name__)
clientApp.register_blueprint(path)          # make app and register routes

clientApp.config["MONGO_URI"] = "mongodb://localhost:27017/medInfoDB"
medInfo.init_app(clientApp)


if (__name__) == '__main__':
    clientApp.run(debug=True)               # run app, refresh whenever changes are made live

