from planet import Planet
from player import Player
from item import Item
from alien import Alien
import os
import updater

player = Player()


def create_world():
    # Set up planets
    a = Planet("Ferenginar")
    b = Planet("Andoria")
    c = Planet("Vulcan")
    d = Planet("Betazed")
    e = Planet("Khitomer")
    f = Planet("Dytallix B")
    Planet.connect_planets(a, "east", b, "west")
    Planet.connect_planets(c, "east", d, "west")
    Planet.connect_planets(a, "north", c, "south")
    Planet.connect_planets(b, "north", d, "south")
    Planet.connect_planets(e, "south", b, "north")
    Planet.connect_planets(f, "west", e, "east")

    # Add some loot to the world
    i = Item("Rock", "This is just a rock.")
    i.put_on_planet(b)
    
    # Player starts here
    player.location = a

    # Define some aliens
    Alien(
        "Quark",
        "Ferengi",
        20,
        a,
        False,
        0.25,
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations. Of course, it's hard not to miss thier very large ears too.",
    )
    Alien(
        "Shras",
        "Andorian",
        20,
        b,
        False,
        0.15,
        "Andorians are militaristic species-- but they never fight without reason, and they despise dishonesy."
    )
    Alien(
        "Sarek",
        "Vulcan",
        20,
        c,
        False,
        0,
        "This species values logic and self-control very highly. Vulcans are known for always behaving logically, and "
        "for never showing emotions, at least not directly. They have long been members of the Federation and human "
        "allies.",
    )
    Alien(
        "Deanna Troi",
        "Betazed",
        20,
        d,
        False,
        .15,
        "Known for being telegraphic, Betazoids are often also able to project their thoughts and sometimes even "
        "maniplate others with them.."
    )
    Alien(
        "Tomalek",
        "Romulan",
        20,
        e,
        False,
        .7,
        "This species is violent, deceitful, and Xenophobic. Alternating between hostility and isolationism, Romulans "
        "will still resort to diplomacy ocassionally when the situation calls for it."
    )
    Alien(
        "2 of 128",
        "Borg",
        50,
        f,
        False,
        1,
        "The Borg are an entirely collective species of cybernetic humanoid species. When they encounter a new species "
        "they assimilate thier biological and technological distinctiveness. Resistance is (generally) futile."
    )

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def print_situation():
    clear()
    print(f"You are on {player.location.desc}")
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
                case "me":
                    print(player.get_status())
                    print()
                    command_success = False
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
        # can uncomment this time_passes block when I decide what I want it to do. In the mean time,
        # commenting it out fixes the duplicate alients bug
        # if time_passes == True:
            # updater.update_all()
