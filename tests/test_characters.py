import unittest
import modules.characters as characters
import modules.objects as obj


class TestCharacters(unittest.TestCase):
    def setUp(self):
        self.character = characters.Character("test name")


class TestCharacterInit(TestCharacters):
    def test_initial_weapon(self):
        self.assertEqual(self.character.weapon, None)

    def test_initial_armour(self):
        self.assertEqual(self.character.armour, [])


# Tests for the player object
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = characters.Player("test username", "test player")

class TestPlayerInit(TestPlayer):
    def test_initial_hp(self):
        if self.player.type == "Balanced":
            self.assertEqual(self.player.hp, 100)
        elif self.player.type == "ADC":
            self.assertEqual(self.player.hp, 50)
        elif self.player.type == "Tank":
            self.assertEqual(self.player.hp, 150)

class TestPlayerDie(TestPlayer):

    def test_empty_inventory(self):
        self.player.die(characters.FloorGuardian())
        self.assertEqual(self.player.inventory, {'armour': [], 'potion': [], 'weapon': []})

    def test_location_after_death(self):
        self.player.die(characters.FloorGuardian())
        self.assertEqual(self.player.current_location, "1a")

    def test_inventory_transfer_to_enemy(self):
        monster = characters.FloorGuardian()
        inventory_items = []
        for x in self.player.inventory:
            for item in self.player.inventory[x]:
                inventory_items.append(item)

        self.player.die(monster)
        assert obj.PlayerLootBox(monster.level, inventory_items, self.player) in monster.player_loot_boxes


class TestFloorGuardian(unittest.TestCase):
    def setUp(self):
        self.floor_guardian = characters.FloorGuardian()

class TestFloorGuardianInit(TestFloorGuardian):
    def test_default_name(self):
        assert self.floor_guardian.name == f"Level {self.floor_guardian.level} {self.floor_guardian.type.capitalize()}"

