class Player:
    def __init__(self, pseudo, civilization, wood, gold, food, capacity):
        self.pseudo= pseudo
        self.civilization = civilization
        self.wood = wood
        self.gold = gold
        self.food = food
        self.capacity = capacity
        

        
        
        
class Building:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def build(self):
        print(f'{self.name} is building')
        
    def destroy(self):
        print(f'{self.name} is destroying')
        
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'{self.name} is moving to {self.x} and {self.y}')
        
    def __repr__(self):
        return f'{self.name} is at {self.x} and {self.y}'
    
    
class House(Building):
    def __init__(self, name, x, y, rooms):
        super().__init__(name, x, y)
        self.rooms = rooms
    


class Barrack(Building):
    def __init__(self, name, x, y, capacity):
        super().__init__(name, x, y)
        self.capacity = capacity
        
        
        
class Farm(Building):
    def __init__(self, name, x, y, farm_type):
        super().__init__(name, x, y)
        self.farm_type = farm_type
        


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
            
    def affiche_map(self):
        for row in self.game_map:
            print(row)
            
    def ajouter_barrack(self, x, y):
        self.game_map[x][y] = "🏢"
        self.affiche_map()
        
    def ajouter_house(self, x, y):
        self.game_map[x][y] = "🏠"
        self.affiche_map()
        
    def ajouter_farm(self, x, y):
        self.game_map[x][y] = "🏡"
        self.affiche_map()  
        


class Civilization:
    def __init__(self, name, buildings, map):
        self.name = name
        self.buildings = buildings
        self.map = map
        
    def build(self, building):
        self.buildings.append(building)
        print(f'{building.name} has been added to the civilization')
        
    def destroy(self, building):
        self.buildings.remove(building)
        print(f'{building.name} has been removed from the civilization')
        
    def show_buildings(self):
        for building in self.buildings:
            print(building)
            
    def show_map(self):
        self.map.affiche_map()
        
        
class French(Civilization):
    def __init__(self, name, buildings, map):
        super().__init__(name, buildings, map)
        
    def build(self, building):
        if isinstance(building, House):
            super().build(building)
        else:
            print('You can only build houses')
            
    def show_buildings(self):
        for building in self.buildings:
            if isinstance(building, House):
                print(building)
                
                
class English(Civilization):
    def __init__(self, name, buildings, map):
        super().__init__(name, buildings, map)
        
    def build(self, building):
        if isinstance(building, Barrack):
            super().build(building)
        else:
            print('You can only build barrack')
            
    def show_buildings(self):
        for building in self.buildings:
            if isinstance(building, Barrack):
                print(building)
            
            
class Unit :
    def __init__(self, name, damage, health, place,deplacement, distance_attack):
        self.name = name
        self.damage = damage
        self.health = health
        self.place = place   
        self.deplacement = deplacement
        self.distance_attack = distance_attack

class Archer(Unit):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def attack(self):
        print(f'{self.name} is attacking')
        
    def move(self):
        print(f'{self.name} is moving')
        
class Warrior(Unit):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def attack(self):
        print(f'{self.name} is attacking')
        
    def move(self):
        print(f'{self.name} is moving')
 
class Siege_Unit:
    def __init__(self, name, damage, health, place):
        self.name = name
        self.damage = damage
        self.health = health
        self.place = place
        
    def attack(self):
        print(f'{self.name} is attacking')
        
    def move(self):
        print(f'{self.name} is moving')       
        
class balista(Siege_Unit):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        
    def attack(self):
        print(f'{self.name} is attacking')
        
    def move(self):
        print(f'{self.name} is moving')