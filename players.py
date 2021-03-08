#!flask/bin/python
from flask import Flask, jsonify
from flask_restful import Api, Resource

class Players(Resource):
    def get(self):
        return jsonify( { "name": "Magnus Carlsen"}, { "name": "Hikaru Nakamura"}, { "name":"Wesley So"}, { "name":"Anish Giri"}, { "name":"Levy Rozman"})
 