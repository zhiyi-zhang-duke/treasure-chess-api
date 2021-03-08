from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from openings import Openings
from players import Players
from games import Games
from puzzles import Puzzles

app = Flask(__name__)
api = Api(app)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

api.add_resource(Openings, '/openings')

# @app.route('/players', methods = ['GET'])
api.add_resource(Players, '/players')

# @app.route('/puzzles', methods = ['GET'])
api.add_resource(Puzzles, '/puzzles')

# @app.route('/games', methods = ['GET'])
api.add_resource(Games, '/games')

if __name__ == "__main__":
    app.run(port=5000)