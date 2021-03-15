from flask import Flask, session, render_template, request, redirect
from os import walk
from os.path import basename
from database.models import Game

import io
import json
import pickle
import chess.pgn

class OpeningsLoader:
    def __init__(self, path="./data/openings/"):
        self.path = path

    def loadDB(self):
        print("Initializing OpeningsLoader")    

        file_data = self.preProcessGamesData()
        print("Current games folder data size:")
        print(len(file_data))

        # To do: remove truncation
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
        #Adds all files in specified path to pgns array
        for (dirpath, dirnames, filenames) in walk(self.path):
            pgns.extend(filenames)
        pgns = [self.path+filename for filename in pgns]

        #Creates chess.pgn games out of all games in pgn file
        chesspgn_games = []
        opening_type_list = []
        for pgn_path in pgns:
            
            pgn_file = open(pgn_path)
            opening_name = basename(pgn_file.name)[0:-4].replace("_", " ")
            
            while game := chess.pgn.read_game(pgn_file):
                chesspgn_games.append(game)
                opening_type_list.append(opening_name)

        #Creates a list of maps representing each game's data
        game_list = []
        for i,game in enumerate(chesspgn_games):
            game_list.append(self.convertGameToMap(game, opening_type_list[i]))

        return game_list

    def convertGameToMap(self, game, opening=""):
        moves = []
        game_map = self.createEmptyGameMap()
        board = game.board()

        for i, move in enumerate(game.mainline_moves()):
            move_str = move.uci()
            moves.append("{}-{}".format(move_str[0:2],move_str[2:]))
        game_map["Moves"]=moves        

        for detail in game.headers:
            game_map[detail]=game.headers[detail]

        if opening:
            game_map["Opening"] = opening

        # print(game_map)
        return game_map

    def createEmptyGameMap(self):
        game_map = {'Event': "", 'Site': "", 'BlackElo': "",
         'BlackFideId': "", 'BlackTitle': "", 'EventDate': "",
         'Opening': "", 'Variation': "", 'WhiteElo': "",
         'WhiteFideId': "", 'WhiteTitle': "", 'Moves': [], 'Date': "",
         'ECO': "", 'Round': "", 'White': "", 'Black': "", 'Result': ""}
        return game_map
