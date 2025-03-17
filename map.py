import numpy as np
# from game import build


game_map = np.zeros((30, 30), dtype=object)


def create_map():
    game_map[4][15] = "🏛️"
    game_map[25][15] = "🏛️"
    for i in range(5):
        for sublist in game_map:
            random_index = np.random.randint(0, len(sublist) - 1)  
            sublist[random_index] = '🗻'
    for row in game_map:
        print(row)
        
        
def affiche_map(game_map):
    for row in game_map:
        print(row)
        

def ajouter_barrack(x, y, game_map, build):
    if game_map[x][y] != 0:
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏢"
        affiche_map(game_map)
    
def ajouter_house(x, y, game_map, build):
    if game_map[x][y] != 0:
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏠"
        affiche_map(game_map)
    
def ajouter_farm(x, y, game_map, build):
    if game_map[x][y] != 0:
        print("Already a building here")
        build()
    else:
        game_map[x][y] = "🏡"
        affiche_map(game_map)
    
    
    

    