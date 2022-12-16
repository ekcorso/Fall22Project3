import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")

    def put_on_planet(self, planet):
        self.loc = planet
        planet.add_item(self)

# This class might be obsolete now
class Weapon(Item):
    def __init__(self, name, desc, damage):
        super().__init__(name, desc)
        self.damage = damage # amount of damage this weapon will do
        self.amunition = 10 # num of times this weapon can be used

    def fire(self, target):
        if self.amunition != 0:
            target.health -= self.damage
            self.amunition -= 1
            # the player should notice if their weapon stop working, so handling the "else" side of this check can be 
            # done at the call site, if at all
