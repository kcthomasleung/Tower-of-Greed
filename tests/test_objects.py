import unittest
import modules.objects as obj

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.weapon = obj.Weapon("test name", 99)


class TestWeaponInit(TestWeapon):
    def test_name(self):
        self.assertEqual(self.weapon.name, "test name")

    def test_type(self):
        self.assertEqual(self.weapon.type, "weapon")

    def test_power(self):
        self.assertEqual(self.weapon.power, 99)

    def test_id(self):
        self.assertEqual(self.weapon.id, "wetestname99.0")


class TestArmour(unittest.TestCase):
    def setUp(self):
        self.armour = obj.Armour("test name", 99, "head")


class TestArmourInit(TestArmour):
    def test_name(self):
        self.assertEqual(self.armour.name, "test name")

    def test_type(self):
        self.assertEqual(self.armour.type, "armour")

    def test_defence(self):
        self.assertEqual(self.armour.defence, 99)

    def test_id(self):
        self.assertEqual(self.armour.id, "artestname99.0head")