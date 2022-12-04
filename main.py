from planet import Planet
from player import Player
from item import Item
from alien import Alien
import os
import updater

player = Player()


def create_world():
    a = Planet("You are on planet 1")
    b = Planet("You are on planet 2")
    c = Planet("You are on planet 3")
    d = Planet("You are on planet 4")
    Planet.connect_planets(a, "east", b, "west")
    Planet.connect_planets(c, "east", d, "west")
    Planet.connect_planets(a, "north", c, "south")
    Planet.connect_planets(b, "north", d, "south")
    i = Item("Rock", "This is just a rock.")
    i.put_on_planet(b)
    player.location = a
    # Note that the line-break below will need to be fixed
    Alien(
        "Quark",
        "Ferengi",
        20,
        a,
        False,
        0.1,
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations.",
    )


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_situation():
    clear()
    print(player.location.desc)
    print()
    if player.location.has_aliens():
        print("This planet is inhabited by the following aliens:")
        for m in player.location.aliens:
            print(f"{m.name}: {m.species}. {m.description}")
        print()
    if player.location.has_items():
        print("This planet has the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exit_names():
        print(e)
    print()


def show_help():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("quit -- quits the game")
    print()
    input("Press enter to continue...")


if __name__ == "__main__":
    create_world()
    playing = True
    while playing and player.alive:
        print_situation()
        command_success = False
        time_passes = False
        while not command_success:
            command_success = True
            command = input("What now? ")
            if len(command) == 0:
                continue
            command_words = command.split()
            if len(command_words) == 0:
                continue
            match command_words[0].lower():
                case "go":  # cannot handle multi-word directions
                    okay = player.go_direction(command_words[1])
                    if okay:
                        time_passes = True
                    else:
                        print("You can't go that way.")
                        command_success = False
                case "pickup":  # can handle multi-word objects
                    target_name = command[7:]  # everything after "pickup "
                    target = player.location.get_item_by_name(target_name)
                    if target != False:
                        player.pickup(target)
                    else:
                        print("No such item.")
                        command_success = False
                case "inventory":
                    player.show_inventory()
                case "help":
                    show_help()
                case "exit":
                    playing = False
                case "attack":
                    target_name = command[7:]
                    target = player.location.get_alien_by_name(target_name)
                    if target != False:
                        player.attack_alien(target)
                    else:
                        print("No such alien.")
                        command_success = False
                case other:
                    print("Not a valid command")
                    command_success = False
        if time_passes == True:
            updater.update_all()
