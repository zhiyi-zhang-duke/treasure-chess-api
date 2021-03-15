from flask import Response, request, jsonify
from database.models import Game
from flask_restful import Resource
import json

class GamesApi(Resource):
    def get(self):
        games = Game.objects().to_json()
        return Response(games, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        game = Game(**body).save()
        id = game.id
        return {'id': str(id)}, 200


class GameApi(Resource):
    def get(self, id):
        game = Game.objects.get(id=id).to_json()
        return Response(game, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Game.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Game.objects.get(id=id).delete()
        return '', 200

class OpeningApi(Resource):
    def get(self):
        openings = Game.objects.distinct(field="opening")
        print(openings)
        message = "Found {} openings.".format(len(openings))
        return jsonify(
            message=message,
            data = openings,
            category = "success",
            status = 200
        )
        # return Response(openings, mimetype="application/json", status=200)

class OpeningsApi(Resource):
    def get(self, name):
        games = Game.objects(opening=name).to_json()
        print(games)
        return Response(games, mimetype="application/json", status=200)
     