import alien
import planet
import player
import item


def test_me_command():
    my_player = player.Player()

    my_player.location = planet.Planet("Vulcan")
    my_player.items = [item.Item("Rock", "This is just a rock")]

    assert my_player.get_status() == "Health: 50. Location: Vulcan. Items: Rock.", "Status not working correctly"
    my_player.items.append(item.Item("Phaser", "This is a badass phaser"))
    assert my_player.get_status() == "Health: 50. Location: Vulcan. Items: Rock, Phaser.", "Status not working correctly"

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


