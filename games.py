#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource

class Games(Resource):
    def get(self):
        return jsonify( { "Coming soon!": "" } )
 