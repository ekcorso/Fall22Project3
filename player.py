import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 50
        self.alive = True

    # goes in specified direction if possible, returns True
    # if not possible returns False
    def go_direction(self, direction):
        new_location = self.location.get_destination(direction.lower())
        if new_location is not None:
            self.location = new_location
            return True
        return False

    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.remove_item(item)

    def show_inventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    def attack_alien(self, alien):
        clear()
        print("You are attacking " + alien.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(alien.name + "'s health is " + str(alien.health) + ".")
        print()
        if self.health > alien.health:
            self.health -= alien.health
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
