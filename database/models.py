from .db import db

class Game(db.Document):
    event = db.StringField(required=True)
    site = db.StringField(required=True)
    date = db.StringField(required=True)
    #round is a keyword, so we are using stage here
    stage = db.StringField(required=True)
    white = db.StringField(required=True)
    black = db.StringField(required=True)
    result = db.StringField(required=True)
    black_elo = db.StringField(required=False)
    blackfide_id = db.StringField(required=False)
    black_title = db.StringField(required=False)
    eco = db.StringField(required=True)
    event_date = db.StringField(required=False)
    opening = db.StringField(required=False)
    variation = db.StringField(required=False)
    white_elo = db.StringField(required=False)
    whitefide_id = db.StringField(required=False)
    white_title = db.StringField(required=False)
    moves = db.ListField(db.StringField(), required=True)
    # moves = db.StringField(required=True)


