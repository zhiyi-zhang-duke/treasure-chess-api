from flask import Flask, session, render_template, request, redirect
from os import walk
from database.models import Game

import io
import json
import pickle
import chess.pgn

class GamesLoader:
    def __init__(self, path="./data/games/"):
        self.path = path

    def loadDB(self):
        print("Initializing GamesLoader")

        print("Checking Game Document...")
        if Game.objects.first():
            print("Found existing Game objects, deleting...")
            Game.objects().delete()        

        file_data = self.preProcessGamesData()
        print("Current games folder data size:")
        print(len(file_data))

        #To do: remove truncation
        for gameMap in file_data[0:3]:
            game = Game(
                event=gameMap['Event'],
                site=gameMap['Site'],
                date=gameMap['Date'], 
                stage=gameMap['Round'],
                white=gameMap['White'],
                black=gameMap['Black'],
                result=gameMap['Result'],
                black_elo=gameMap['BlackElo'],
                blackfide_id=gameMap['BlackFideId'],
                black_title=gameMap['BlackTitle'],
                eco=gameMap['ECO'],
                event_date=gameMap['EventDate'],
                opening=gameMap['Opening'],
                variation=gameMap['Variation'],
                white_elo=gameMap['WhiteElo'],
                whitefide_id=gameMap['WhiteFideId'],
                white_title=gameMap['WhiteTitle'],
                moves=gameMap['Moves']
                )
            game.save()
        print("Database loaded successfully!")


    def preProcessGamesData(self):
        pgns = []
        for (dirpath, dirnames, filenames) in walk(self.path):
            pgns.extend(filenames)
        pgns = [self.path+filename for filename in pgns]

        chesspgn_games = []
        for pgn_path in pgns:
            pgn_file = open(pgn_path)
            while game := chess.pgn.read_game(pgn_file):
                chesspgn_games.append(game)

        game_list = []
        for game in chesspgn_games:
            game_list.append(self.convertGameToMap(game))

        # print(pgns)
        # print(game_list)
        # return json.dumps(game_list)
        return game_list

    def convertGameToMap(self, game):
        # To do: This is a workaround for array of strings not mapping
        # correctly in a javascript response
        moves = []
        game_map = {}
        board = game.board()

        # move_csv = ""
        # for i, move in enumerate(game.mainline_moves()):
        #     move_str = move.uci()
        #     if i==0:
        #         move_csv += ("{}-{}".format(move_str[0:2],move_str[2:]))
        #     else:
        #         #Chess.js formatting
        #         move_csv += (",{}-{}".format(move_str[0:2],move_str[2:]))
        # game_map["Moves"]=move_csv
        for i, move in enumerate(game.mainline_moves()):
            move_str = move.uci()
            moves.append("{}-{}".format(move_str[0:2],move_str[2:]))
        game_map["Moves"]=moves        
        
        for detail in game.headers:
            game_map[detail]=game.headers[detail]

        # print(game_map)
        return game_map