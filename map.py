import numpy as np
import pandas as pd
from classe import Player
from classe import Townhall
from classe import Barrack
from classe import House
from classe import Farm
from classe import Building
from classe import Warrior
from classe import Archer

game_map = np.zeros((10, 10), dtype=object)

pd.options.display.float_format = '{:.0f}'.format
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None
pd.options.display.colheader_justify = 'center'


Player1 = Player("Player 1","", 0, 0, 0, 0)
Player2 = Player("Player 2","", 0, 0, 0, 0)
townhall1 = Townhall(x=2, y=5, owner=Player1)
townhall2 = Townhall(x=8, y=5, owner=Player2)


def create_map(game_map):
    for i in range(2):
        for sublist in game_map:
            random_index = np.random.randint(0, len(sublist) - 1)
            sublist[random_index] = '🗻'        
    game_map[2][5] = townhall1.icon
    game_map[8][5] = townhall2.icon
    game_map = pd.DataFrame(game_map, index=range(10), columns=range(10))
    game_map.replace(0, '', inplace=True)
    print(game_map)
    return game_map
    
    
def is_taken(x, y,game_map):
    if game_map[x][y] != 0:
        return True
    else:
        return False
        
def affiche_map(game_map):
    game_map = pd.DataFrame(game_map, index=range(10), columns=range(10))
    print(game_map)
    return game_map
        

def ajouter_barrack(x, y, game_map, build, player):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        barrack = Barrack(x=x, y=y, owner=player)
        game_map[x][y] = barrack.icon
        print(f"Barrack added by {player.name} at ({x}, {y})")
        affiche_map(game_map)
        
def ajouter_house(x, y, game_map, build, player):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        house = House(x=x, y=y, owner=player)
        game_map[x][y] = house.icon
        print(f"House added by {player.name} at ({x}, {y})")
        affiche_map(game_map)

def ajouter_farm(x, y, game_map, build, player):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        farm = Farm(x=x, y=y, owner=player)
        game_map[x][y] = farm.icon
        print(f"Farm added by {player.name} at ({x}, {y})")
        affiche_map(game_map)


def create_soldier(barrack: Barrack, game_map, player):
    if not isinstance(barrack, Barrack):
        raise TypeError("Expected a Barrack object for the 'barrack' parameter.")
    x = barrack.x + 1
    y = barrack.y + 1
    if x < len(game_map) and y < len(game_map[0]) and game_map[x][y] == '':
        print("Creating a soldier...")
        soldier = Warrior(x=x, y=y, owner=player)
        game_map[x][y] = soldier.icon
        print(f"Soldier created by {player.name} at ({x}, {y})")
        affiche_map(game_map)
    else:
        print("Cannot create a soldier here. The position is occupied or out of bounds.")

def create_archer(barrack, game_map, player):
    x = barrack.x + 1
    y = barrack.y + 1
    if x < len(game_map) and y < len(game_map[0]) and game_map[x][y] == '':
        print("Creating an archer...")
        archer = Archer(x=x, y=y, owner=player)
        game_map[x][y] = archer.icon
        print(f"Archer created by {player.name} at ({x}, {y})")
        affiche_map(game_map)
    else:
        print("Cannot create an archer here. The position is occupied or out of bounds.")
    