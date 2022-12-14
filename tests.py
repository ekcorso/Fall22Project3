import alien
import planet
import player
import item


def test_me_command():
    my_player = player.Player()

    my_player.location = planet.Planet("Vulcan")
    my_player.items = [item.Item("Rock", "This is just a rock")]

    assert my_player.get_status() == "Health: 100. Location: Vulcan. Items: Rock.", "Status not working correctly"
    my_player.items.append(item.Item("Phaser", "This is a badass phaser"))
    assert my_player.get_status() == "Health: 100. Location: Vulcan. Items: Rock, Phaser.", "Status not working correctly"

def test_weapon():
    my_player = player.Player()
    vulcan = planet.Planet("Vulcan")
    my_player.location = vulcan

    phaser = item.Weapon("Phaser", "This is a badass phaser", 5)
    phaser.put_on_planet(vulcan)
    my_player.pickup(phaser)
    
    quark = alien.Alien(
        "Quark",
        "Ferengi",
        20,
        vulcan,
        False,
        0.25,
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations. Of course, it's hard not to miss thier very large ears too.",
    )

    phaser.fire(quark)
    assert quark.health == 15, "Weapon not doing damage correctly"
    assert phaser.amunition == 9, "Amunition is not depleting correctly"


def test_attacking_pre_warp():
    my_player = player.Player()
    vulcan = planet.Planet("Vulcan")
    my_player.location = vulcan

    kes = alien.Alien(
        "Kes",
        "Ocampa",
        15,
        vulcan,
        True,
        0.25,
        "The Ocampa are a humanoid, pre-warp species. After an accident damanged their planet's atmosphere they were"
        "underground and only survived with the help of the Caretaker, a benevolent member of a more advanced species."
    )

    daggin = alien.Alien(
        "Daggin",
        "Ocampa",
        15,
        vulcan,
        True,
        0.25,
        "The Ocampa are a humanoid, pre-warp species. After an accident damanged their planet's atmosphere they were"
        "underground and only survived with the help of the Caretaker, a benevolent member of a more advanced species."
    ) 

    pre_warp_penalty = lambda: .95
    no_pre_warp_penalty = lambda: .5

    my_player.attack_alien(kes, pre_warp_penalty)
    assert vulcan.get_alien_by_name(kes.name) is False, "Kes didn't die"
    assert my_player.health == 80, "Something is wrong with damage assessment with pre warp penality"
    my_player.attack_alien(daggin, no_pre_warp_penalty)
    assert vulcan.get_alien_by_name(daggin.name) is False, "Daggin didn't die"
    assert my_player.health == 65, "Something is wrong with damage assessment with no pre warp penality"


def test_shields_raised():
    my_player = player.Player()
    vulcan = planet.Planet("Vulcan")
    my_player.location = vulcan

    quark = alien.Alien(
        "Quark",
        "Ferengi",
        20,
        vulcan,
        False,
        0.25,
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations. Of course, it's hard not to miss thier very large ears too.",
    )

    nog = alien.Alien(
        "Nog",
        "Ferengi",
        20,
        vulcan,
        False,
        0.25,
        "This species prizes business acumen. While Ferengi are not inherently hostile, they will persue profit at "
        "all costs in most negotiations. Of course, it's hard not to miss thier very large ears too.",
    )

    my_player.raise_shields()
    my_player.attack_alien(quark)
    assert my_player.health == 90, "Incorrect damage after raising shields"
    my_player.lower_shields()
    my_player.attack_alien(nog)
    assert my_player.health == 70, "Incorrect damange with shields lowered"
