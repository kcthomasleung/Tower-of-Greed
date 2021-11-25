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

    def __str__(self):
        return(f'''ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Power: {self.power}
        ''')

class Armour(Item):
    def __init__(self, name, defence, body_part, type="armour"):
        super().__init__(name, type)
        self.defence = defence
        self.body_part = body_part
        self.set_id()

    def __str__(self):
        return(f'''ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Defence Power: {self.defence}
        ''')

class Potion(Item):
    def __init__(self, name, type="potion"):
        super().__init__(name, type)
        self.heal = 100
        self.set_id()

    def __str__(self):
        return(f'''ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Heal Power: {self.heal}
        ''')


class LootBox:
    def __init__(self, level):
        self.id = ""
        self.level = level
        self.content = None
        self.set_id()
        self.set_default_content()

    def set_id(self):
        self.id = f"{self.level}"

    def set_default_content(self):
        if self.level % 5 == 0:
            weapon_power = 2 ** (self.level/7) + 3 * self.level
            weapon = Weapon(f"Level {self.level} Sword", weapon_power)
            self.content = [weapon]
        else:
            armour_defence = 2 ** (self.level/6.3) + 3 * self.level
            armour = Armour(f"Level {self.level} Armour", armour_defence, "torso")
            self.content = [armour]

    def __str__(self):
        return f'''
    ID: {self.id}
    Contents: {self.content}'''


class PlayerLootBox():
    # This class is a player specific loot box. Only players with the certain username will be able to open this loot box
    def __init__(self, level, content,  player):
        self.id = ""
        self.level = level
        self.content = content
        self.player = player
        self.set_id()

    def set_id(self):
        self.id = f"{self.level}{self.player.username}"

    def __str__(self):
        return f'''
    ID: {self.id}
    Contents: {self.content}'''



sword = Weapon("Sword", 100)
baseball_bat = Weapon("Baseball Bat", 15)

metal_helmet = Armour("Metal Helmet", 50, "head")
scarf = Armour("Scarf", 5, "neck")
vest = Armour("Vest", 70, "torso")
breast_plate = Armour("Breast Plate", 150, "torso")
gauntlet = Armour("Gauntlet", 60, "hand")
armlet = Armour("Armlet", 90, "arm")
cuisse = Armour("Cuisse", 90, "leg")

health_potion = Potion("Health Potion")

# print(sword.name, sword.type, sword.id)

# loot_box1 = LootBox(5)
# print(loot_box1.content[0])
