from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from database.db import initialize_db
from resources.routes import initialize_routes
from games_loader import GamesLoader
from openings_loader import OpeningsLoader


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/treasure-chess'
}

# Previous routes I had
# api.add_resource(Openings, '/openings')

# # @app.route('/players', methods = ['GET'])
# api.add_resource(Players, '/players')

# # @app.route('/puzzles', methods = ['GET'])
# api.add_resource(Puzzles, '/puzzles')

# # @app.route('/games', methods = ['GET'])
# api.add_resource(Games, '/games')

initialize_db(app)
initialize_routes(api)


if __name__ == "__main__":
    #To do: Change this to load new game document
    #Maybe try static data first
    gl = GamesLoader("./data/games/")
    gl.loadDB()

    ol = OpeningsLoader("./data/openings/")
    ol.loadDB()

    app.run(port=5000)