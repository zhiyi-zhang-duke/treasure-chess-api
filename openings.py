#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource

class Openings(Resource):
    def get(self):
        return jsonify( { 'name': 'Queen\'s Gambit', 'side': 'white'} ) 