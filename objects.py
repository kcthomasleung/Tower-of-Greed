class Item:
    def __init__(self, name, type):
        self.id = ""
        self.name = name
        self.type = type
        self.heal = None
        self.defence = None
        self.power = None


    def set_id(self):
        # this method gives each item an item id based on their type, name, and stats
        item_name = self.name
        id_name = item_name.replace(" ","")

        if self.type == "weapon":
            self.id = f"we{id_name}{self.power}"
        elif self.type == "armour":
            self.id = f"ar{id_name}{self.defence}"
        elif self.type == "potion":
            self.id = f"po{id_name}{self.heal}"
        else:
            print("Error: Invalid item type")


class Weapon(Item):
    def __init__(self, name, power, type="weapon"):
        super().__init__( name, type)
        self.power = power
        self.set_id()


class Armour(Item):
    def __init__(self, name, defence, type="armour"):
        super().__init__(name, type)
        self.defence = defence
        self.set_id()


class Potion(Item):
    def __init__(self, name, type="potion"):
        super().__init__(name, type)
        self.heal = 100
        self.set_id()

# class LootBox:


sword = Weapon("Baseball Bat", 50)
print(sword.name, sword.type, sword.id)