import random
import updater


class Alien:
    def __init__(
        self, name, species, health, planet, is_pre_warp, hostility, description=""
    ):
        self.name = name
        self.species = species
        self.health = health
        self.planet = planet
        self.is_pre_warp = is_pre_warp  # Bool
        self.hostility = hostility  # Float between 0-1
        self.description = description
        planet.add_alien(self)
        updater.register(self)

    def update(self):
        # this is what is causing the aliens to move around and sometimes have multiple in one room
        if random.random() < 0.5:
            self.move_to(self.planet.random_neighbor())

    def move_to(self, planet):
        self.planet.remove_alien(self)
        self.planet = planet
        planet.add_alien(self)

    def die(self):
        self.planet.remove_alien(self)
        updater.deregister(self)
