import re
import json

def file_parser():
  # Faz a leitura da linha do arquivo
  path = 'src/database/games.log'
  file = open(path, 'r')
  lines = file.read().splitlines()
    
  return lines

def new_game():
    game_index = str(len(games)+1)
    game_key = 'game_'+game_index
    games[game_key] = {
      'total_kills': 0,
      'players': [],
      'kills': {}
    }
    
    return game_key

def new_player(game_key, line):
  # Obtem o nome do player que se conectou
  regex = re.compile(r'[\\]')
  line = regex.split(line)
  new_player = line[1]
    
  if new_player not in games[game_key]['players'] and new_player != '<world>':
    games[game_key]['players'].append(new_player)
    games[game_key]['kills'][new_player] = 0
    

def get_kill_and_died_player(kill):
  kill = kill.split(' ')[4:-2]
  killed_index = kill.index('killed')
  player_killed = ''.join(kill[:killed_index])\
                    if len(kill[:killed_index]) < 2 else ' '.join(kill[:killed_index])
  player_died = ''.join(kill[(killed_index+1):])\
                    if len(kill[(killed_index+1):]) < 2 else ' '.join(kill[(killed_index+1):])  

  return (player_killed, player_died)
  
def new_kill(game_key, line):
  player_killed, player_died = get_kill_and_died_player(line)
    
  if player_killed == '<world>':
    games[game_key]['kills'][player_died] -= 1
  elif player_killed != player_died and player_killed != '<world>':
    games[game_key]['kills'][player_killed] += 1
  
  games[game_key]['total_kills'] += 1

parsed_file = file_parser()

games = {}
game_key = ''

for index, line in enumerate(parsed_file):
  line = line[7:].strip()
  
  if line[0] == '-':
    continue
  
  action_separator_index = line.index(':')
  action = line[0:action_separator_index]
  
  if action == 'InitGame':
    game_key = new_game()
  elif action == 'ClientUserinfoChanged':
    new_player(game_key, line)
  elif action == 'Kill':
    new_kill(game_key, line)