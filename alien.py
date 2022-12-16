import random
import updater


class Alien:
    def __init__(
        self, name, species, health, planet, is_pre_warp, resource_needed, resource_request, description=""
    ):
        self.name = name
        self.species = species
        self.health = health
        self.planet = planet
        self.is_pre_warp = is_pre_warp  # Bool
        self.description = description
        self.resource_needed = resource_needed
        self.resource_request = resource_request
        self.negotiation_attempted = False
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

    def request_resources(self):
        print()
        print(f"{self.name}: \"{self.resource_request}\"")
        print()
        # print("Hint: try \"give\" + the name of the item being requested")
