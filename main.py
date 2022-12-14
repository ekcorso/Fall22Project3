from planet import Planet
from player import Player
from item import Item
from alien import Alien
import os
import updater
import random

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
    Planet.connect_planets(e, "north", b, "south")
    Planet.connect_planets(f, "east", e, "west")

    # Add some resources to the world
    dilithium = Item("Dilithium Crystal", "Initially a scarce resource, dilithium crystals were shown to be an "
                     "essential component for a starship's faster than light drive, or warp drive, since they were "
                     "necessary to regulate the matter-antimatter reactions needed to generate the required energy.")
    cordrazine = Item("Cordrazine", "This is a powerful stimulant used to revive patients in an emergency. Overdoses "
                      "cause hallucinations, madness and death.")
    latinum = Item("Gold-pressed latinum", "Latinum is a medium of exchange or currency used by the Ferengi and others. "
                   "Latinum was useful as a medium of exchange, unlike the (worthless) gold in which it was enclosed, "
                   "because it is impossible to replicate.")
    trellium = Item("Trellium-D", "Trellium-D is an alloy used in the Delphic Expanse as a protection against spatial "
                    "anomalies.")
    tritanium = Item("Tritanium", "A very common item, tritanium is an extremely hard alloy used in starship hulls "
                     "and many hand-held tools.")
    dilithium.put_on_planet(b)
    cordrazine.put_on_planet(a)
    latinum.put_on_planet(d)
    trellium.put_on_planet(e)
    tritanium.put_on_planet(c)

    # Player starts here
    player.location = random.choice([a, b, c, d, e])

    # Define some aliens
    Alien(
        "Quark",
        "Ferengi",
        20,
        a,
        False,
        latinum,
        "I'll owe you a favor, Hu-mon, if you can lend me a few bars of latinum. Do we have a deal?",
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations. Of course, it's hard not to miss thier very large ears too.",
    )
    Alien(
        "Kes",
        "Ocampa",
        15,
        b,
        True,
        cordrazine,
        "My brother was hurt and is badly in need of medical treatment. With all of your technological ability, can "
        "you help us? Our doctor tells me that just one vial of cordrazine could save his life."
        "The Ocampa are a humanoid, pre-warp species. After an accident damanged their planet's atmosphere they were"
        "underground and only survived with the help of the Caretaker, a benevolent member of a more advanced species."
    )
    # Alien(
        # "Shras",
        # "Andorian",
        # 20,
        # b,
        # False,
        # cordrazine,
        # "My second-in-command was in an accident and needs emergency medical treatment. I'd be happy to set "
        # "aside our differences if you can give us a few vials of cordrazine to treat him. What do you say?",
        # "Andorians are militaristic species-- but they never fight without reason, and they despise dishonesy."
    # )
    Alien(
        "Sarek",
        "Vulcan",
        20,
        c,
        False,
        tritanium,
        "Our ship was damaged in battle and is badly in need of repair. Can you spare some tritanium to help us fix it?",
        "This species values logic and self-control very highly. Vulcans are known for always behaving logically, and "
        "for never showing emotions, at least not directly. They have long been members of the Federation and human "
        "allies.",
    )
    Alien(
        "Lwaxana",
        "Betazed",
        15,
        d,
        False,
        dilithium,
        "Now Captain I know you can be reasonable about this. My ship's dilithium crystals have ceased to function ever "
        "since we passed through the Rosette Nebula. I know you have a little extra dilithium on board, won't you be "
        "a dear and share it with my ship? Come on, I know you will help us..",
        "Known for being telepathic, Betazoids are often also able to project their thoughts and sometimes even "
        "maniplate others with them.."
    )
    Alien(
        "Tomalek",
        "Romulan",
        30,
        e,
        False,
        trellium,
        "My ship will be passing through the Delphic Expanse soon-- I don't know if we'll make it through the anomaly "
        "unless we can get enough Trellium-D to fortify our vessle. Captain to captain, can you help me save my crew?",
        "This species is violent, deceitful, and Xenophobic. Alternating between hostility and isolationism, Romulans "
        "will still resort to diplomacy ocassionally when the situation calls for it."
    )
    Alien(
        "2 of 128",
        "Borg",
        90,
        f,
        False,
        None,
        "We are the Borg. Resistance is futile-- lower your shields and surrender. You will be assimilated",
        "The Borg are an entirely collective species of cybernetic humanoid species. When they encounter a new species "
        "they assimilate thier biological and technological distinctiveness. Resistance is generally futile."
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
            print(f"{i.name} -- {i.desc}")
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
    print("negotiate -- attemp to negotiate with the nearby alien")
    print("give <item> -- gives this item to alien you are currently negotiating with")
    print("raise shields -- protect yourself in case of attack")
    print("lower shields -- lower your shields after an attack")
    print("quit -- quits the game")
    print()
    input("Press enter to continue...")

def print_initial_setup():
    print("Space: The final frontier.")
    print()
    print("You are the Captain of a starship. You are on a mission to explore strange new worlds, to seek out "
          "new life and new civilizations, to boldly go where no one has gone before.")
    print()
    print("Start by exploring as many planets as you can. You can interact with the alien species and artifacts you "
          "find there, but beware: not all aliens are friendly. Also note that your Federation does not condone "
          "interacting with species that have not yet developed warp capabilities, even though it is sometimes "
          "necessary.")
    print()
    print("Hint: type 'help' if you get stuck")
    print()
    input("Press enter to begin exploring...")

if __name__ == "__main__":
    create_world()
    playing = True
    print_initial_setup()
    while playing and player.alive and not player.has_won:
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
                    if target is not False:
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
                case "raise":
                    # raise shields
                    print("Your shields are up")
                    print()
                    player.raise_shields()
                    command_success = False
                case "lower":
                    # lower shields
                    print("Your shields are down")
                    print()
                    player.lower_shields()
                    command_success = False
                case "give":
                    resource = command[5:]  # this is the item name str
                    found_item = False
                    for item in player.items:
                        if item.name.lower() == resource.lower():
                            player.give_item(item, player.location.aliens[0])
                            found_item = True
                    if found_item is False:
                        print("Hmmm it doesn't look like you have that item...")
                case "negotiate":
                    player.negotiate()
                    if not player.has_won:
                        command_success = False
                case "quit":
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
