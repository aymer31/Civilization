

class Player:
    def __init__(self, name, civilization, wood, gold, food, capacity):
        self.name = name
        self.civilization = civilization
        self.wood = wood
        self.gold = gold
        self.food = food
        self.capacity = capacity
        self.townhall = Townhall(x=0, y=0, owner=self)
    
    def own_barrack(self):
        for building in self.civilization.buildings:
            if isinstance(building, Barrack):
                return building
        return None
    
        
        
class Building:
    def __init__(self, ID, name, x, y, health, level, owner, icon, wood, gold, food, capacity,price_wood,price_gold,price_food):
        self.ID = ID
        self.name = name
        self.x = x
        self.y = y
        self.health = health
        self.level = level
        self.owner = owner
        self.icon = icon
        self.wood = wood
        self.gold = gold
        self.food = food
        self.capacity = capacity
        self.price_wood = price_wood
        self.price_gold = price_gold    
        self.price_food = price_food
        
    def build(self):
        print(f'{self.name} is building')
        
    def destroy(self):
        print(f'{self.name} is destroying')
        
    
        
    def __repr__(self):
        return f'{self.name} is at {self.x} and {self.y}'
    
    
    
class Townhall(Building):
    def __init__(self, x, y, owner):
        super().__init__(
            ID=None,
            name="Townhall",
            x=x,
            y=y,
            health=1000,
            level=1,
            owner=owner,
            icon="🏛️",
            wood=200,
            gold=100,
            food=50,
            capacity=10,
            price_food=0,
            price_gold=0,
            price_wood=0
        )
    
class House(Building):
    def __init__(self, x, y, owner):
        super().__init__(
            ID = None,
            name = "House",
            x = x,
            y = y,
            health = 400,
            level=1,
            owner=owner,
            icon="🏠",
            wood=200,
            gold=100,
            food = 50,
            capacity = 7,
            price_food=100,
            price_gold=50,
            price_wood=150
        )


class Barrack(Building):
    def __init__(self, x, y, owner):
        super().__init__(
            ID=None,
            name="Barrack",
            x=x,
            y=y,
            health=200,
            level=1,
            owner=owner,
            icon="🏢",
            wood=200,
            gold=100,
            food=50,
            capacity=5,
            price_food=100,
            price_gold=50,
            price_wood=150
        )
        
        
        
class Farm(Building):
    def __init__(self, x, y, owner):
        super().__init__(
            ID=None,
            name="Farm",
            x=x,
            y=y,
            health=1000,
            level=1,
            owner=owner,
            icon="🏡",
            wood=200,
            gold=100,
            food=50,
            capacity=2,
            price_food=100,
            price_gold=50,
            price_wood=150
        )
        


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
            
    def affiche_map(self):
        for row in self.game_map:
            print(row)
            
    def ajouter_barrack(self, x, y, player):
        self.game_map[x][y] = "🏢"
        player.civilization.build(Barrack(x, y, player))
        self.affiche_map()

    def ajouter_house(self, x, y, player):
        self.game_map[x][y] = "🏠"
        player.civilization.build(House(x, y, player))
        self.affiche_map()

    def ajouter_farm(self, x, y, player):
        self.game_map[x][y] = "🏡"
        player.civilization.build(Farm(x, y, player))
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
            
            
class Unit:
    def __init__(self, ID, name, damage, health, place, deplacement, distance_attack, x, y, owner):
        self.ID = ID
        self.name = name
        self.damage = damage
        self.health = health
        self.place = place
        self.deplacement = deplacement
        self.distance_attack = distance_attack
        self.x = x
        self.y = y
        self.owner = owner

    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'{self.name} is moving to {self.x} and {self.y}')

    def attack(self, target):
        print(f'{self.name} is attacking {target.name} causing {self.damage} damage')

    def __repr__(self):
        return f'{self.name} at ({self.x}, {self.y}) with {self.health} health'

class Archer(Unit):
    def __init__(self, x, y,owner):
        super().__init__(
            ID=None,
            name="Farm",
            x=x,
            y=y,
            health=1000,
            level=1,
            owner=owner,
            icon="🏡",
            wood=200,
            gold=100,
            food=50,
            capacity=2,
            price_food=100,
            price_gold=50,
            price_wood=150
        )
        
    def attack(self):
        print(f'{self.name} is attacking with a bow')
        
    def move(self, x, y):
        super().move(x, y)
        print(f'{self.name} moved swiftly to {self.x}, {self.y}')
        

class Warrior(Unit):
    def __init__(self, x, y, owner):
        super().__init__(
            ID=None,
            name="Farm",
            x=x,
            y=y,
            health=1000,
            level=1,
            owner=owner,
            icon="🏡",
            wood=200,
            gold=100,
            food=50,
            capacity=2,
            price_food=100,
            price_gold=50,
            price_wood=150
        )
        
    def attack(self):
        print(f'{self.name} is attacking with a sword')
        
    def move(self, x, y):
        super().move(x, y)
        print(f'{self.name} charged to {self.x}, {self.y}')
 
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