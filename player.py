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
        print(f"You've beamed up the {item.name} and put it in the cargo bay.")
        print()

    def negotiate(self):
        alien = self.location.aliens[0]  # there should be only 1
        print(f"You're attempting to negotiate with {alien.name}...")
        self.diplomacy += 15
        alien.request_resources() 

    def give_item(self, item, alien):
        if item in self.items and alien.resource_needed == item:
            print(f"You are giving {alien.name} the {item.name}.")
            print()
            self.items.remove(item)
            alien.has_resource_needed = True
            self.diplomacy += 20
            print("You have completed this part of your diplomatic mission.")
            input("Press enter to keep exploring the galaxy...")
        else:
            print(f"That's not the item that {alien.name} is looking for.")
            print()
            input("Press enter to continue or try again...")

    def show_inventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    def attack_alien(self, alien, rigged_outcome=None):
        clear()
        print("You are attacking " + alien.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(alien.name + "'s health is " + str(alien.health) + ".")
        print()
        # this is for testing purposes, so I can inject the desired outcome
        if rigged_outcome is None:
            coin_toss_outcome = lambda: random.random()
        else:
            coin_toss_outcome = rigged_outcome
        total_points_lost = alien.health
        if alien.negotiation_attempted is False:
            # player will gain points for negotiating AND lose points for not doing so
            self.diplomacy -= 25
        if self.shields_raised:
            total_points_lost -= 10
        if alien.is_pre_warp:
            coin_toss = coin_toss_outcome()
            if coin_toss >= .8:
                self.diplomacy -= 10  # a slap on the hand from Starfleet
        self.health -= total_points_lost
        if self.health > 0:
            print(f"You win. Your health is now {self.health}. Your diplomacy is now {self.diplomacy}.")
            alien.die()
        else:
            print()
            print("\"It is possible to commit no mistakes and still lose. That is not a weakness. That is life.\""
                  "-- Captain Jean-Luc Picard")
            print("(But the game is over now.)")
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
