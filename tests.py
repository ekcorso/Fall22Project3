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

