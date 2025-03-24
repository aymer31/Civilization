from map import create_map
from map import ajouter_barrack
from map import ajouter_house
from map import ajouter_farm
from map import affiche_map
from map import game_map

start = False

def game():
    global start
    if start:
        print("Welcome to Civilization VII!")
        print("1. Start Game")
        print("2. Load Game")
        print("4. Stats")
        print("5. Règles")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Starting game...")
            New_game()
            
        elif choice == "2":
            Load_game()
        elif choice == "4":
            print("Stats:")
        elif choice == "5":
            règles = open("règles.txt", "r")
            print(règles.read())
            règles.close()
        elif choice == "6":
            print("Exiting game...")
            start = False
        else:
            print("Invalid choice, please try again.")
            
def Mod():
    global start
    print("Choose the mode :")
    print("1. PvP")
    print("2. You against AI")
    print("3. AI against AI")
    print("4. Menu")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("PvP mode")
        PvP()
    elif choice == "2":
        print("You against AI mode")
        AI_Fight()
    elif choice == "3":
        print("AI against AI mode")
        AI_AI()
    elif choice == "4":
        game()
    elif choice == "5":
        print("Exiting game...")
        start = False
    else:
        print("Invalid choice, please try again.")

        
    
def PvP():
    create_map(game_map)
    playing_PvP()
    
    
def AI_Fight():
    create_map(game_map)
    playing_Ai_Fight()
    
def AI_AI():
    create_map(game_map)
    playing_Ai_Ai()
    
        
def playing_PvP():
    while start == True:
        print("Player 1 turn")
        action()
        print("Player 1 turn end")
        print("Player 2 turn")
        action()
        print("Player 2 turn end")
        
        
        
    
def playing_Ai_Fight():
    print("You against AI mode")

def playing_Ai_Ai():
    print("AI against AI mode")


def action():
    global start
    print("Choose an action:")
    print("1. Move")
    print("2. Attack")
    print("3. Build")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Moving...")
        affiche_map(game_map)
    elif choice == "2":
        print("Attacking...")
        affiche_map(game_map)
    elif choice == "3":
        print("Building...")
        build()
        print("Choose an action:")
        print("1. Move")
        print("2. Attack")
        choice = input("Enter choice: ")
    elif choice == "4":
        print("Do you want to save the game ?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter choice: ")
        if choice == "1":
            print("Saving game...")
            start = False
        elif choice == "2":
            print("Not saving game...")
            start = False
        else:
            print("Invalid choice, please try again.")
            start = False
    else:
        print("Invalid choice, please try again.")
        action()
        
def build():
    print("Choose what to build:")
    print("1. House")
    print("2. Farm")
    print("3. Barrack")
    choice = input("Enter choice: ")
    if choice == "1":
        print("Building house...")
        print("Which location ?")
        choice_x = int(input("longueur: "))
        choice_y = int(input("largeur: "))
        print (choice_x, choice_y)
        if 0 <= choice_x < len(game_map) and 0 <= choice_y < len(game_map[0]):
            ajouter_house(choice_x, choice_y, game_map, build)
        else:
            print("Invalid location, please try again.")
        
    elif choice == "2":
        print("Building farm...")
        choice_x = int(input("longueur: "))
        choice_y = int(input("largeur: "))
        if 0 <= choice_x < len(game_map) and 0 <= choice_y < len(game_map[0]):
            ajouter_farm(choice_x, choice_y, game_map, build)
        else:
            print("Invalid location, please try again.")
    elif choice == "3":
        print("Building barrack...")
        print("Which location ?")
        choice_x = int(input("longueur: "))
        choice_y = int(input("largeur: "))
        ajouter_barrack(choice_x, choice_y, game_map, build)
        

def New_game():
    print("Creating new game...")
    Mod()
    
    
def Load_game():
    print("Loading game...")
    create_map(game_map)

def start_game():
    global start
    start = True
    game()

if __name__ == "__main__":
    start_game()
