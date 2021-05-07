from flask import Flask, Response, request
from src.api.parse import (games)
import json

app = Flask('__main__')

@app.route('/api/v1/ping', methods=['GET'])
def ping():
  return { 'ping': 'pong' }

@app.route('/api/v1/games', methods=['GET'])
def get_all_games():
  
  return json.dumps(games)

@app.route('/api/v1/games/<int:id>', methods=['GET'])
def find_game(id):
  
  game = games[f'game_{game_id}']
  
  return json.dumps(game)
  

app.run()