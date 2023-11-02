from flask import Flask                     # import Flask application
from medInfo import medInfo           # import Flask customized PyMongo from MongoDB
from clientApp_routes import path           # import the routes blueprint from clientApp_routes
import json
from flask_pymongo import PyMongo

clientApp = Flask(__name__)
clientApp.register_blueprint(path)          # make app and register routes

clientApp.config["MONGO_URI"] = "mongodb://localhost:27017/"
medInfo.init_app(clientApp)

@clientApp.before_first_request
def checkDB():
    try:
        local = medInfo.db
        localName = local.name  # Get the database name

        # Check if the database exists on the local server
        if localName not in local.client.list_database_names():
            # Database doesn't exist on the local server, so create it
    
            print(f"Database '{localName}' does not exist. Creating...")

            # Copy data from included json files
            with open(r"C:\Users\19295\projects\Flask Web Application\medInfoDB.Patients.json", "r") as json_file1:
                data = json.load(json_file1)
                local.Patients.insert_many(data)
            
            print(f"Database '{localName}' created.")

    except PyMongo.errors.ServerSelectionTimeoutError:
        # Handle connection errors (e.g., the local server is not reachable)
        print("Failed to connect to the local MongoDB server")


if (__name__) == '__main__':
    clientApp.run(debug=True)               # run app, refresh whenever changes are made live

