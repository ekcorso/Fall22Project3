import os
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 100
        self.diplomacy = 50
        self.alive = True
        self.shields_raised = False

    # goes in specified direction if possible, returns True
    # if not possible returns False
    def go_direction(self, direction):
        new_location = self.location.get_destination(direction.lower())
        if new_location is not None:
            self.location = new_location
            return True
        return False

    def raise_shields(self):
        self.shields_raised = True

    def lower_shields(self):
        self.shields_raised = False

    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.remove_item(item)

       

    def give_item(self, item, alien):
        if item in self.items and alien.resource_needed == item:
            print(f"You are giving {alien.name} the {item.name}.")
            print()
            self.items.remove(item)
            alien.has_resource_needed = True
            self.diplomacy += 20
            print("You have completed this part of your diplomatic mission.")
            input("Press enter to keep exploring the galaxy...")

    def show_inventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    def attack_alien(self, alien, rigged_outcome=None):
        # let's incorporate losing diplomacy points here, as well as using weapons, taking less damage if
        # the shields are up (the player will need to manually raise shields before an attack)
        # will also need an is_pre_warp check
        clear()
        print("You are attacking " + alien.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(alien.name + "'s health is " + str(alien.health) + ".")
        print()
        if rigged_outcome is None:
            coin_toss_outcome = lambda: random.random()
        else:
            coin_toss_outcome = rigged_outcome
        total_points_lost = alien.health
        if self.shields_raised:
            total_points_lost -= 10
        if alien.is_pre_warp:
            coin_toss = coin_toss_outcome()
            if coin_toss >= .8:
                total_points_lost += 5  # a slap on the hand from Starfleet
        self.health -= total_points_lost
        if self.health > 0:
            print("You win. Your health is now " + str(self.health) + ".")
            alien.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

    def get_status(self):
        """Returns a string with the player's current stats"""
        mapped_list = [item.name for item in self.items]
        item_str = ""
        if len(mapped_list) != 0:
            index = 0
            for item in mapped_list:
                if index != len(mapped_list) - 1:
                    item_str += f"{str(item)}, "
                else:
                    item_str += f"{str(item)}"
                index += 1
        else:
            item_str = "Empty"
        status_str = (
            f"Health: {self.health}. Location: {self.location.desc}. Items: {item_str}."
        )
        return status_str
