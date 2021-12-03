import re


class Item:
    def __init__(self, name, type):
        self.id = ""
        self.name = name
        self.type = type
        self.heal = float
        self.defence = float
        self.power = float

    def set_id(self):
        # this method gives each item an item id based on their type, name, and stats
        item_name = self.name
        id_name = item_name.replace(" ", "")

        if self.type == "weapon":
            self.id = f"we{id_name}{self.power}"
        elif self.type == "armour":
            self.id = f"ar{id_name}{self.defence}{self.body_part}"
        elif self.type == "potion":
            self.id = f"po{id_name}{self.heal}"
        else:
            print("Error: Invalid item type")


class Weapon(Item):
    def __init__(self, name, power, type="weapon"):
        super().__init__(name, type)
        self.power = float(power)
        self.set_id()

    def __str__(self):
        return f"""ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Power: {self.power}
        """


class Armour(Item):
    def __init__(self, name, defence, body_part, type="armour"):
        super().__init__(name, type)
        self.defence = float(defence)
        self.body_part = ""
        self.set_body_part(body_part)
        self.set_id()

    def set_body_part(self, body_part):
        # this method ensures the passed body_part parameter is valid, and will raise an error otherwise
        if (
            body_part != "head"
            and body_part != "neck"
            and body_part != "torso"
            and body_part != "arm"
            and body_part != "hand"
            and body_part != "leg"
        ):
            raise Exception("Body part of armour invalid")

        else:
            self.body_part = body_part

    def __str__(self):
        return f"""ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Defence Power: {self.defence}
        """


class Potion(Item):
    def __init__(self, name, type="potion"):
        super().__init__(name, type)
        self.heal = float(100)
        self.set_id()

    def __str__(self):
        return f"""ID: {self.id}    Type: {self.type.capitalize()}   Name: {self.name}   Heal Power: {self.heal}
        """


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
        # this method sets the default content of each lootbox according to the level they are at
        if self.level % 5 == 0:
            weapon_power = round(2 ** (self.level / 7) + 3 * self.level, 2)
            weapon = Weapon(f"Level {self.level} Sword", weapon_power)
            self.content = [weapon]
        else:
            armour_defence = round(2 ** (self.level / 6.3) + 3 * self.level, 2)
            armour = Armour(f"Level {self.level} Armour", armour_defence, "torso")
            self.content = [armour]

    def __str__(self):
        return f"""
    ID: {self.id}
    Contents: {self.content}"""


class PlayerLootBox:
    # This class is a player specific loot box. Only players with the certain username will be able to open this loot box
    def __init__(self, level, content, player):
        self.id = ""
        self.level = level
        self.content = content
        self.player = player
        self.set_id()

    def set_id(self):
        self.id = f"{self.level}{self.player.username}"

    def __str__(self):
        return f"""
    ID: {self.id}
    Contents: {self.content}"""


def create_item_with_id(id):
    # This method is to make creating items in the game easier by just passing in a item id

    # find the item_type of the item (identified by the first two characters of the item id)
    item_type = id[:2]

    # find the item stat of the item (the only floats in item ids)
    item_stat = re.findall("[+-]?\d+\.\d+", id)[
        0
    ]  # source: https://stackoverflow.com/questions/44939027/how-to-find-a-float-in-a-string-python

    # find the item name from the item id (in between item_type and item_stat)
    item_name = id[
        id.find(item_type) + len(item_type) : id.rfind(item_stat)
    ]  # source: https://stackoverflow.com/questions/3368969/find-string-between-two-substrings

    # add spaces between capitalised letters for the item name
    spaced_name = re.sub(
        r"(\w)([A-Z])", r"\1 \2", item_name
    )  # source: https://stackoverflow.com/questions/199059/a-pythonic-way-to-insert-a-space-before-capital-letters

    if item_type == "we":
        weapon = Weapon(spaced_name, float(item_stat))
        return weapon
    elif item_type == "ar":
        # each armour has a specific body_part it corresponds to. The following line is to find out the body_part of the armour using the item id
        item_body_part = id.split(f"{item_stat}")[1]
        armour = Armour(spaced_name, item_stat, item_body_part)
        return armour
    elif item_type == "po":
        potion = Potion(spaced_name)
        return potion
    else:
        print("Error: item id invalid")


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

# print(health_potion)

loot_box1 = LootBox(5)
# print(loot_box1)


# item_type = metal_helmet.id[:2]
# item_stat = re.findall("[+-]?\d+\.\d+", metal_helmet.id)[0]
# item_name = metal_helmet.id[
#     metal_helmet.id.find(item_type) + len(item_type) : metal_helmet.id.rfind(item_stat)
# ]
# item_body_part = metal_helmet.id.split(f"{item_stat}")[1]

# better_name = re.sub(r"(\w)([A-Z])", r"\1 \2", item_name)
# print(metal_helmet)
# print(item_stat)
# print(better_name)

# armour = create_item_with_id("poHealthPotion100")
# print(armour)
