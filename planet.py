import random

class Planet:
    def __init__(self, description):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
    def add_exit(self, exit_name, destination):
        self.exits.append([exit_name, destination])
    def get_destination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
        return self
    def connect_planets(planet1, dir1, planet2, dir2):
        #creates "dir1" exit from planet1 to planet2 and vice versa
        planet1.add_exit(dir1, planet2)
        planet2.add_exit(dir2, planet1)
    def exit_names(self):
        return [x[0] for x in self.exits]
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def add_monster(self, monster):
        self.monsters.append(monster)
    def remove_monster(self, monster):
        self.monsters.remove(monster)
    def has_items(self):
        return self.items != []
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def has_monsters(self):
        return self.monsters != []
    def get_monster_by_name(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def random_neighbor(self):
        return random.choice(self.exits)[1]
