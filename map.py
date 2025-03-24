import numpy as np
import pandas as pd


game_map = np.zeros((30, 30), dtype=object)

pd.options.display.float_format = '{:.0f}'.format
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None
pd.options.display.colheader_justify = 'center'





def create_map(game_map):
    for i in range(5):
        for sublist in game_map:
            random_index = np.random.randint(0, len(sublist) - 1)
            sublist[random_index] = '🗻'        
    game_map[4][15] = "🏛️"
    game_map[25][15] = "🏛️"
    game_map = pd.DataFrame(game_map, index=range(30), columns=range(30))
    game_map.replace(0, '', inplace=True)
    print(game_map)
    return game_map
    
    
def is_taken(x, y,game_map):
    if game_map[x][y] != 0:
        return True
    else:
        return False
        
def affiche_map(game_map):
    game_map = pd.DataFrame(game_map, index=range(30), columns=range(30))
    print(game_map)
    return game_map
        

def ajouter_barrack(x, y, game_map, build):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏢"
        affiche_map(game_map)
    
def ajouter_house(x, y, game_map, build):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏠"
        affiche_map(game_map)
    
def ajouter_farm(x, y, game_map, build):
    if game_map[x][y] != '':
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏡"
        affiche_map(game_map)
