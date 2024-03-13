#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, make_response, jsonify, request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Combat, Status, Character, Player, KnownTech, Technique
from gameplay_methods import begin_combat


# Views go here!


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Login(Resource):
    def post(self):
        player = Player.query.filter(
            Player.name == request.get_json()['name']
        ).first()
        if player:
            session['player_id'] = player.id
            response = make_response(player.to_dict(), 200)
        else:
            response = make_response({}, 404)
        
        return response

class Logout(Resource):
    def delete(self):
        session['player_id'] = None
        response = make_response({}, 204)
        return response

class CheckSession(Resource):

    def get(self):
        player = Player.query.filter(Player.id == session.get('player_id')).first()
        if player:
            response = make_response(player.to_dict(), 200)
        else:
            response = make_response({}, 401)
        return response

api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

