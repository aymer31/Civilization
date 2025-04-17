import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import json
from datetime import datetime
from tkinter import Tk, Canvas, Button, Label, StringVar
import random
import time

game_map = np.full((10, 10), '', dtype=object)
pd.options.display.max_columns = None

class Player:
    def __init__(self, name, civilization, wood=500, gold=500, food=500, capacity=10):
        self.name = name
        self.civilization = civilization
        self.wood = wood
        self.gold = gold
        self.food = food
        self.capacity = capacity
        self.units = []
        self.own_barrack = None
        self.own_house = None
        self.own_farm = None
        self.townhall = Townhall(0, 0, self)

class Building:
    def __init__(self, name, x, y, health, owner, icon, price_wood, price_gold, price_food,food_production,gold_production,wood_production):
        
        self.name = name
        self.x = x
        self.y = y
        self.health = health
        self.owner = owner
        self.icon = icon
        self.price_wood = price_wood
        self.price_gold = price_gold
        self.price_food = price_food
        self.food_production = food_production
        self.gold_production = gold_production
        self.wood_production = wood_production

class Townhall(Building):
    def __init__(self, x, y, owner):
        super().__init__('Townhall', x, y, 1000, owner, '🏛️', 0, 0, 0, 0, 1000, 0)

class House(Building):
    def __init__(self, x, y, owner):
        super().__init__('House', x, y, 400, owner, '🏠', 150, 50, 100, 0, 0, 1000)

class Barrack(Building):
    def __init__(self, x, y, owner):
        super().__init__('Barrack', x, y, 300, owner, '🏢', 150, 50, 100, 0, 0, 0)

class Farm(Building):
    def __init__(self, x, y, owner):
        super().__init__('Farm', x, y, 250, owner, '🏡', 150, 50, 100, 1000, 0, 0)

class Unit:
    def __init__(self, name, x, y, health, damage, owner, icon, attack_range, movement_range, price_wood, price_gold, price_food):
        self.name = name
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.owner = owner
        self.icon = icon
        self.attack_range = attack_range
        self.movement_range = movement_range
        self.price_food = price_food
        self.price_wood = price_wood
        self.price_gold = price_gold

    def move(self, new_x, new_y):
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1:
            if game_map[new_x][new_y] not in ['', '⬜']:
                print("Case occupée !")
                return
            game_map[self.x][self.y] = ''
            self.x = new_x
            self.y = new_y
            game_map[self.x][self.y] = self.icon
            print(f"{self.name} moved to ({self.x}, {self.y})")
        else:
            print("Move too far!")

    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} attacks {target.name} for {self.damage} damage!")

class Warrior(Unit):
    def __init__(self, x, y, owner):
        super().__init__('Warrior', x, y, 100, 5000, owner, '⚔️', 1, 1, 250, 450, 500)

class Archer(Unit):
    def __init__(self, x, y, owner):
        super().__init__('Archer', x, y, 80, 3000, owner, '🏹',3 , 2, 450, 250, 500)
        
class GameGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Civilization Game")
            self.canvas = Canvas(root, width=500, height=500, bg="white")
            self.canvas.grid(row=0, column=0, columnspan=4)
            self.info_label = Label(root, text="Welcome to Civilization Game!")
            self.info_label.grid(row=1, column=0, columnspan=4)
            self.turn_label = StringVar()
            self.turn_label.set("Player 1's Turn")
            self.turn_display = Label(root, textvariable=self.turn_label)
            self.turn_display.grid(row=2, column=0, columnspan=4)
            self.build_button = Button(root, text="Build", command=self.build_action)
            self.build_button.grid(row=3, column=0)
            self.move_button = Button(root, text="Move Unit", command=self.move_action)
            self.move_button.grid(row=3, column=1)
            self.attack_button = Button(root, text="Attack", command=self.attack_action)
            self.attack_button.grid(row=3, column=2)
            self.generate_button = Button(root, text="Generate Unit", command=self.generate_action)
            self.generate_button.grid(row=3, column=3)
            self.current_player = player1
            self.update_map()

        def update_map(self):
            self.canvas.delete("all")
            for i in range(10):
                for j in range(10):
                    x0, y0 = j * 50, i * 50
                    x1, y1 = x0 + 50, y0 + 50
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
                    if game_map[i][j] != '' and game_map[i][j] != '⬜':
                        self.canvas.create_text(x0 + 25, y0 + 25, text=game_map[i][j], font=("Arial", 16))

        def build_action(self):
            build(self.current_player)
            self.update_map()
            self.next_turn()

        def move_action(self):
            move_unit(self.current_player)
            self.update_map()
            self.next_turn()

        def attack_action(self):
            attack(self.current_player)
            self.update_map()
            self.next_turn()

        def generate_action(self):
            generate_unit(self.current_player)
            self.update_map()
            self.next_turn()

        def next_turn(self):
            self.current_player = player2 if self.current_player == player1 else player1
            self.turn_label.set(f"{self.current_player.name}'s Turn")

def main_gui():
        player1.name = input("Nom Joueur 1: ")
        print("Choisissez la civilisation de Joueur 1:")
        print("1. French\n2. English")
        civ1 = input("Choix: ")
        player1.civilization = "French" if civ1 == "1" else "English"

        player2.name = input("Nom Joueur 2: ")
        print("Choisissez la civilisation de Joueur 2:")
        print("1. French\n2. English")
        civ2 = input("Choix: ")
        player2.civilization = "French" if civ2 == "1" else "English"

        root = Tk()
        GameGUI(root)
        root.mainloop()
        
        




player1 = Player("", "French")
player2 = Player("", "English")

player1.townhall.x, player1.townhall.y = 2, 5
player2.townhall.x, player2.townhall.y = 8, 5
game_map[2][5] = player1.townhall.icon
game_map[8][5] = player2.townhall.icon

event_log = []

def show_map():
    df = pd.DataFrame(game_map, index=[f"L{i}" for i in range(10)], columns=[f"C{j}" for j in range(10)])
    df.replace('', '⬜', inplace=True)
    print(df.to_string())

def build(player):
    while True:
        print("1. House\n2. Farm\n3. Barrack")
        c = input("Choix: ")
        x = int(input("X: "))
        y = int(input("Y: "))
        if game_map[x][y] not in ['', '⬜']:
            print("Case occupée! Veuillez choisir une autre action.")
            continue
        if c == '1':
            b = House(x, y, player)
            player.own_house = b
        elif c == '2':
            b = Farm(x, y, player)
            player.own_farm = b
        elif c == '3':
            b = Barrack(x, y, player)
            player.own_barrack = b
        else:
            print("Choix invalide")
            continue
        if player.wood < b.price_wood or player.gold < b.price_gold or player.food < b.price_food:
            print("Ressources insuffisantes pour construire ce bâtiment.")
            continue
        player.wood -= b.price_wood
        player.gold -= b.price_gold
        player.food -= b.price_food
        game_map[x][y] = b.icon
        log_event(player, "Build", f"{b.name} at ({x}, {y})", '')
        print(f"{b.name} construit à ({x}, {y}).")
        print(f"Ressources restantes de {player.name} - Bois: {player.wood}, Or: {player.gold}, Nourriture: {player.food}")
        break


def has_barrack(player):
    return player.own_barrack is not None


def has_house(player):
    return player.own_house is not None

def has_farm(player):
    return player.own_farm is not None

def end_game(winner):
    print(f"\n🎉 {winner.name} gagne !")
    with open("game_log.json", "w") as f:
        json.dump(event_log, f, indent=2)
    df = pd.DataFrame(event_log)
    df['action'].value_counts().plot(kind='bar')
    plt.title("Statistiques de la partie")
    plt.show()
    exit()

def generate_unit(player):
        if not player.own_barrack:
            print("Vous devez construire une caserne pour générer des troupes.")
            return
        print("1. Warrior\n2. Archer")
        choice = input("Choix: ")
        x, y = player.own_barrack.x + 1, player.own_barrack.y
        if game_map[x][y] not in ['', '⬜']:
            x += 1  
            if game_map[x][y] not in ['', '⬜']:
                print("déplacer d'abord une troupe")
                take_turn(player)
                
            
        if choice == '1':
            unit = Warrior(x, y, player)
            player.food -= unit.price_food
            player.wood -= unit.price_wood
            player.gold -= unit.price_gold
        elif choice == '2':
            unit = Archer(x, y, player)

            player.food -= unit.price_food
            player.wood -= unit.price_wood
            player.gold -= unit.price_gold
        else:
            print("Choix invalide")
            return
        if len(player.units) >= player.capacity:
            print("Capacité maximale atteinte. Construisez plus de maisons.")
            return
        player.units.append(unit)
        game_map[x][y] = unit.icon
        log_event(player, "Generate Unit", f"{unit.name} at ({x}, {y})", '')
        print(f"{unit.name} généré à ({x}, {y}).")

def move_unit(player):
    print("Sélectionnez une unité à déplacer:")
    for i, unit in enumerate(player.units):
        print(f"{i + 1}. {unit.name} ({unit.x}, {unit.y})")
    choice = int(input("Choix: ")) - 1
    if choice < 0 or choice >= len(player.units):
        print("Choix invalide.")
        return
    unit = player.units[choice]
    print("Choisissez une direction:")
    print("1. Haut\n2. Bas\n3. Gauche\n4. Droite")
    direction = input("Direction: ")
    if direction == '1':
        new_x, new_y = unit.x - unit.movement_range, unit.y
    elif direction == '2':
        new_x, new_y = unit.x + unit.movement_range, unit.y
    elif direction == '3':
        new_x, new_y = unit.x, unit.y - unit.movement_range
    elif direction == '4':
        new_x, new_y = unit.x, unit.y + unit.movement_range
    else:
        print("Direction invalide.")
        return
    log_event(player, "Moved Unit", f"{unit.name} at ({new_x}, {new_y})", '')
    unit.move(new_x, new_y)
    
    
def attack(player):
    print("Sélectionnez une unité pour attaquer:")
    for i, unit in enumerate(player.units):
        print(f"{i + 1}. {unit.name} ({unit.x}, {unit.y})")
    choice = int(input("Choix: ")) - 1
    if choice < 0 or choice >= len(player.units):
        print("Choix invalide.")
        return
    unit = player.units[choice]
    targets = []
    for dx in range(-unit.attack_range, unit.attack_range + 1):
        for dy in range(-unit.attack_range, unit.attack_range + 1):
            target_x, target_y = unit.x + dx, unit.y + dy
            if 0 <= target_x < game_map.shape[0] and 0 <= target_y < game_map.shape[1]:
                if game_map[target_x][target_y] not in ['', '⬜']:
                    for p in [player1, player2]:
                        if p != player:
                            for enemy_unit in p.units:
                                if enemy_unit.x == target_x and enemy_unit.y == target_y:
                                    targets.append(enemy_unit)
                            if p.townhall.x == target_x and p.townhall.y == target_y:
                                targets.append(p.townhall)
                            if p.own_barrack and p.own_barrack.x == target_x and p.own_barrack.y == target_y:
                                targets.append(p.own_barrack)
    if not targets:
        print("Aucune cible à portée.")
        return
    print("Cibles disponibles:")
    for i, target in enumerate(targets):
        print(f"{i + 1}. {target.name} ({target.x}, {target.y}) - Santé: {target.health}")
    target_choice = int(input("Choix de la cible: ")) - 1
    if target_choice < 0 or target_choice >= len(targets):
        print("Choix invalide.")
        return
    target = targets[target_choice]
    unit.attack(target)
    log_event(player, "Attacked", f"{unit.name} attacked {target.name} at ({target.x}, {target.y})", target.name)
    if target.health <= 0:
        print(f"{target.name} a été détruit!")
        log_event(player, "Destroy", f"{target.name} at ({target.x}, {target.y})", '')
        if isinstance(target, Townhall):
            log_event(player, "Win", f"Destroyed {target.owner.name} Townhall", '')
            end_game(player)
        else:
            game_map[target.x][target.y] = ''
        log_event(player, "Destroyed", f"{unit.name} destroyed {target.name} at ({target.x}, {target.y})", target.name)
    else:
        print(f"{target.name} a {target.health} points de vie restants.")
    
    
    
def take_turn(player):
    while True:
        print(f"\n{player.name}'s turn ({player.civilization})")
        print("1. Build\n2. Move Unit\n3. Attack\n4. Generate Unit\n5. End Turn")
        choice = input("Choix: ")
        if choice == '1':
            build(player)
            show_map()
            take_turn(player)
        elif choice == '2':
            move_unit(player)
            show_map()
            take_turn(player)
        elif choice == '3':
            attack(player)
            show_map()
            take_turn(player)
        elif choice == '4':
            generate_unit(player)
            show_map()
            take_turn(player)
        elif choice == '5':
            print("Tour terminé.")
            log_event(player, "End Turn", f"{player.name} ended their turn",'')
            break
        else:
            print("Choix invalide")
            


def build_barrack_near_townhall(player):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = player.townhall.x + dx
            y = player.townhall.y + dy
            if 0 <= x < 10 and 0 <= y < 10 and game_map[x][y] in ['', '⬜']:
                input_values = ['3', str(x), str(y)]
                input_iter = iter(input_values)
                input_backup = __builtins__.input
                __builtins__.input = lambda _: next(input_iter)
                try:
                    build(player)
                except:
                    pass
                __builtins__.input = input_backup
                return
            
            
def build_farm_near_townhall(player):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = player.townhall.x + dx
            y = player.townhall.y + dy
            if 0 <= x < 10 and 0 <= y < 10 and game_map[x][y] in ['', '⬜']:
                input_values = ['2', str(x), str(y)]
                input_iter = iter(input_values)
                input_backup = __builtins__.input
                __builtins__.input = lambda _: next(input_iter)
                try:
                    build(player)
                except:
                    pass
                __builtins__.input = input_backup
                return
            
def build_house_near_townhall(player):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = player.townhall.x + dx
            y = player.townhall.y + dy
            if 0 <= x < 10 and 0 <= y < 10 and game_map[x][y] in ['', '⬜']:
                input_values = ['1', str(x), str(y)]
                input_iter = iter(input_values)
                input_backup = __builtins__.input
                __builtins__.input = lambda _: next(input_iter)
                try:
                    build(player)
                except:
                    pass
                __builtins__.input = input_backup
                return

        

def try_attack_with_unit(unit, player):
    enemy = player2 if player == player1 else player1

    townhall = enemy.townhall
    if abs(unit.x - townhall.x) <= unit.attack_range and abs(unit.y - townhall.y) <= unit.attack_range:
        unit.attack(townhall)
        print(f"{unit.name} attaque la Townhall ennemie !")
        if townhall.health <= 0:
            print("🏛️ Townhall détruite !")
            game_map[townhall.x][townhall.y] = ''
            log_event(player, "Win", f"{player.name} a détruit la Townhall ennemie",'')
            end_game(player)
        return True

    for dx in range(-unit.attack_range, unit.attack_range + 1):
        for dy in range(-unit.attack_range, unit.attack_range + 1):
            tx, ty = unit.x + dx, unit.y + dy
            if 0 <= tx < 10 and 0 <= ty < 10:
                for target in enemy.units:
                    if target.x == tx and target.y == ty:
                        unit.attack(target)
                        print(f"{unit.name} attaque {target.name} !")
                        log_event(player, "Attacked", f"{unit.name} attacked {target.name} at ({target.x}, {target.y})", target.name)
                        if target.health <= 0:
                            print(f"{target.name} éliminé !")
                            log_event(player, "Destroyed", f"{unit.name} destroyed {target.name} at ({tx}, {ty})", target.name)
                            game_map[tx][ty] = ''
                            if isinstance(target, Unit):
                                enemy.units.remove(target)
                        return True
    return False


def move_unit_with_strategy(unit, player):
    enemy = player2 if player == player1 else player1
    dx = enemy.townhall.x - unit.x
    dy = enemy.townhall.y - unit.y

    direction_priority = []

    if abs(dx) > abs(dy):
        direction_priority = [(1 if dx > 0 else -1, 0), (0, 1), (0, -1)]
    else:
        direction_priority = [(0, 1 if dy > 0 else -1), (1, 0), (-1, 0)]

    for move_dx, move_dy in direction_priority:
        new_x = unit.x + move_dx
        new_y = unit.y + move_dy
        if 0 <= new_x < 10 and 0 <= new_y < 10 and game_map[new_x][new_y] in ['', '⬜']:
            log_event(player, "Moved Unit", f"{unit.name} at ({new_x}, {new_y})", '')
            unit.move(new_x, new_y)
            return

    print(f"{unit.name} est bloqué.")



def ia_vs_ia_loop():
    players = [player1, player2]

    while True:
        for player in players:
            for building in [player.own_house, player.own_farm, player.own_barrack, player.townhall]:
                if building:
                    player.food += building.food_production
                    player.gold += building.gold_production
                    player.wood += building.wood_production    
            print(f"\n{player.name}'s turn ({player.civilization})")
            print(f"Ressources - Bois: {player.wood}, Or: {player.gold}, Nourriture: {player.food}")

            possible_moves = {}
            for x in range(10):
                for y in range(10):
                    if game_map[x][y] in ['', '⬜']:
                        possible_moves[(x, y)] = 0  

            def evaluate_moves(moves, player):
                enemy = player2 if player == player1 else player1
                for move in moves:
                    x, y = move

                    if (x, y) == (5, 5):
                        moves[move] += 5
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 10 and 0 <= ny < 10:
                                icon = game_map[nx][ny]
                                if icon == enemy.townhall.icon or (enemy.own_barrack and icon == enemy.own_barrack.icon):
                                    moves[move] += 10

                    for unit in player.units:
                        if abs(unit.x - x) <= 1 and abs(unit.y - y) <= 1:
                            moves[move] += 3

            evaluate_moves(possible_moves, player)
            try:
                df = pd.read_csv("data.csv")
                for index, row in df.iterrows():
                    if row['action'] == 'Moved Unit':
                        try:
                            details = row['details']
                            if '(' in details:
                                coord = tuple(map(int, details.split('at (')[1].rstrip(')').split(', ')))
                                if coord in possible_moves:
                                    if 'Win' in df[df['id_partie'] == row['id_partie']]['action'].values:
                                        possible_moves[coord] += 15
                        except:
                            continue
            except FileNotFoundError:
                pass  

            if possible_moves:
                best_move = max(possible_moves, key=possible_moves.get)
                print(f"📍 IA {player.name} préfère jouer vers {best_move}")

            
            if not has_barrack(player) and player.wood >= 150 and player.gold >= 50 and player.food >= 100:
                build_barrack_near_townhall(player)
                show_map()

            if not has_farm(player) and player.food < 500:
                build_near_townhall(player, "Farm")
                show_map()
            if not has_house(player) and player.wood < 500:
                build_near_townhall(player, "House")
                show_map()
            if len(player.units) < player.capacity and player.wood >= 500 and player.gold >= 500 and player.food >= 500:
                generate_unit_auto(player)
                show_map()
            for unit in player.units:
                if try_attack_with_unit(unit, player):
                    continue
                move_unit_with_strategy(unit, player)

            log_event(player, "End Turn", f"{player.name} ended their turn", '')
            show_map()
            time.sleep(0.5)


def build_near_townhall(player, building_type):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x = player.townhall.x + dx
            y = player.townhall.y + dy
            if 0 <= x < 10 and 0 <= y < 10 and game_map[x][y] in ['', '⬜']:
                input_values = ['1' if building_type == "House" else '2' if building_type == "Farm" else '3', str(x), str(y)]
                input_iter = iter(input_values)
                input_backup = __builtins__.input
                __builtins__.input = lambda _: next(input_iter)
                try:
                    build(player)
                except:
                    pass
                __builtins__.input = input_backup
                return

            
def choisir_action_depuis_csv(identifiant):
    try:
        df = pd.read_csv("data.csv")
        ligne = df[df['id'] == identifiant]
        if not ligne.empty:
            details = ligne.iloc[0]['details']
            if 'score_choix' in details and '100' in details:
                return ligne.iloc[0]['action']
    except:
        pass
    return None


def generate_unit_auto(player):
    if not player.own_barrack:
        return
    unit_type = random.choice(['1', '2'])  
    input_values = [unit_type]
    input_iter = iter(input_values)
    input_backup = __builtins__.input
    __builtins__.input = lambda _: next(input_iter)
    try:
        generate_unit(player)
    except:
        pass
    __builtins__.input = input_backup



def main():
    print("Choisissez le mode de jeu :")
    print("1. Joueur vs Joueur")
    print("2. IA vs IA")
    mode = input("Choix (1 ou 2) : ")

    if mode == "1":
        player1.name = input("Nom Joueur 1: ")
        print("Choisissez la civilisation de Joueur 1:\n1. French\n2. English")
        civ1 = input("Choix: ")
        player1.civilization = "French" if civ1 == "1" else "English"

        player2.name = input("Nom Joueur 2: ")
        print("Choisissez la civilisation de Joueur 2:\n1. French\n2. English")
        civ2 = input("Choix: ")
        player2.civilization = "French" if civ2 == "1" else "English"

        show_map()
        while True:
            take_turn(player1)
            take_turn(player2)

    elif mode == "2":
        player1.name = "IA_1"
        player2.name = "IA_2"
        player1.civilization = "French"
        player2.civilization = "English"
        show_map()
        ia_vs_ia_loop()
    else:
        print("Choix invalide. Veuillez relancer le jeu.")
        

def end_game(winner):
    print(f"\n🎉 {winner.name} gagne !")
    with open("game_log.json", "w") as f:
        json.dump(event_log, f, indent=2)
    df = pd.DataFrame(event_log)
    df['action'].value_counts().plot(kind='bar')
    plt.title("Statistiques de la partie")
    plt.show()
    exit()


def save_event_log():
    try:
        existing_data = pd.read_csv("data.csv")
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    new_data = pd.DataFrame(event_log)
    combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    combined_data.to_csv("data.csv", index=False, encoding='utf-8')

def log_event(player, action, details,destinataire):
    global event_log, current_game_id
    event_log.append({
        'id_action': len(event_log) + 1,
        'id_partie': current_game_id,
        'time': datetime.now().isoformat(),
        'player': player.name,
        'action': action,
        'details': details,
        'destinatiare': destinataire
    })
    save_event_log()

current_game_id = int(time.time())  

def traiter_events(action_actuelle):
    df = pd.read_csv("data.csv")

    choix_partie = []

    for index, row in df.iterrows():
        if row['action'] == action_actuelle:
            try:
                try:
                    details = json.loads(row['details'])
                except json.JSONDecodeError:
                    print(f"Error decoding JSON for details: {row['details']}")
                    continue
                if 'score_choix' in details:
                    details['score_choix'] += 100
                    df.at[index, 'details'] = str(details)
                    choix_partie.append(row['id'])
            except:
                pass  

    df.to_csv("data.csv", index=False)
    print("choix_partie :", choix_partie)

 
if __name__ == "__main__":
    main()
