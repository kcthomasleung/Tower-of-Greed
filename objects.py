class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Weapon(Item):
    def __init__(self, name, type, hitpoint):
        super().__init__(name, type)
        self.hitpoint = hitpoint


class Armour(Item):
    def __init__(self, name, type, defence):
        super().__init__(name, type)
        self.defence = defence


# class LootBox:
