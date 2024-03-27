from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class message(Resource):
    def get(self):
        return jsonify({"message": "Hi!"})

api.add_resource(message, "/")

if __name__ == "__main__":
    app.run(debug=True)