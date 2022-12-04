import random
import updater

class Alien:
    def __init__(self, name, health, planet):
        self.name = name
        self.health = health
        self.planet = planet
        planet.add_alien(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.move_to(self.planet.random_neighbor())
    def move_to(self, planet):
        self.planet.remove_alien(self)
        self.planet = planet
        planet.add_alien(self)
    def die(self):
        self.planet.remove_alien(self)
        updater.deregister(self)
