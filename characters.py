import re


class Character:
    # This class is to create game characters (i.e. player and monsters)

    def __init__(self, name, type="balanced", gender="M"):
        self.name = name
        self.type = type
        self.hp = float
        self.power = float
        self.gender = gender
        self.armour = []
        self.inventory = None
        # self.hp_regen_rate = 0

    def total_armour(self):
        # This function calculates the total armour of the player
        total = 0
        for i in range(len(self.armour)):
            total += self.armour[i]["defence"]
        return total

    def take_damage(self, damage, enemy):
        # This function handles when a character takes damage from another character
        self.hp -= damage
        if self.hp <= 0:
            # self.die()
            print(f"{self.name} took {damage} damage from {enemy.name}")
            print(f"{self.name} have died")
        else:
            print(f"{self.name} took {damage} damage from {enemy.name}")
            print(f"{self.name}'s current health is {self.hp}")

    def deal_damage(self, enemy):
        # this method manages events when a character attacks another
        # Inspired by the lecture slides, this is to ensure we do not get negative damage
        damage = max(self.power - enemy.total_armour(), 0)
        enemy.hp -= damage
        if enemy.hp <= 0:
            # self.die()
            print(f"{self.name} has dealt {damage} damage to {enemy.name}")
            print(f"{enemy.name} have died")
        else:
            print(f"{self.name} has dealt {damage} damage to {enemy.name}")
            print(f"{enemy.name}'s current health is {enemy.hp}")

    # def hp_regen():


class Player(Character):
    # This class creates a character for the player

    def __init__(
        self,
        username,
        name,
        type="balanced",
        gender="M",
    ):
        super().__init__(name, type, gender)
        self.username = username
        self.inventory = {
            "weapon": [
                {"id": "weSword100", "type": "weapon", "name": "Sword", "power": 100},
                {
                    "id": "weBaseballBat15",
                    "type": "weapon",
                    "name": "Baseball Bat",
                    "power": 15,
                },
            ],
            "armour": [
                {
                    "id": "arMetalHelmet50",
                    "type": "armour",
                    "name": "Metal Helmet",
                    "defence": 50,
                },
                {"id": "arVest70", "type": "armour", "name": "Vest", "defence": 70},
            ],
            "potions": [
                {
                    "id": "poHealthPotion100",
                    "type": "potion",
                    "name": "Health Potion",
                    "heal": 100,
                }
            ],
        }
        self.weapon = {}
        self.current_location = "1a"
        self.floor_access = 1
        self.initial_stats()

    def initial_stats(self):
        # This function takes the player type and determines their initial hp

        if self.type == "Balanced":
            self.hp = 100
            self.power = 5
        elif self.type == "ADC":
            self.hp = 50
            self.power = 10
        elif self.type == "Tank":
            self.hp = 150
            self.power = 2
        else:
            print("Error: Invalid type")

    # This method controls the movements of the player
    def movement(self, destination):

        # Parse the destination string to extract the floor level
        floor_level = int(re.findall("[0-9]+", destination)[0])

        # Check if the player is allowed to travel to the destination passed
        if floor_level > self.floor_access:
            print("You do not have access to this level")
        else:
            self.current_location = destination

    # This function handles what happens after the player has died
    # def die(self, enemy):
    #     # reset player inventory, location, armour, weapon and stats
    #     self.inventory = None
    #     self.current_location = "1a"
    #     self.weapon = {}
    #     self.armour = []
    #     self.initial_stats()

    # def add_to_inventory(self, item):
    #     if item.type == "weapon":
    #         self.inventory["weapon"].append(item)

    def equip_weapon(self, weapon_name):
        # check if the player actually have the specified item in their inventory
        try:
            if not any(
                item["name"] == weapon_name for item in self.inventory["weapon"]
            ):
                print("You do not have this item")

            else:
                # assign temp var for the chosen weapon object to be equiped from the player's inventory
                weapon = next(
                    item
                    for item in self.inventory["weapon"]
                    if item["name"] == weapon_name
                )
                # only one weapon allowed to be equipped at one time. Notify user the equipped weapon will be replaced if
                # they have a weapon already equipped
                if self.weapon:
                    print(
                        "You already have a weapon equipped, it is now replaced with your selected item"
                    )
                    self.weapon = weapon
                else:
                    self.weapon = weapon

                self.power += self.weapon["power"]

        except KeyError:
            print("You do not have any weapons")

    # def equip_armour(self, armour_name):
    # def add_to_inventory(self, item):
    #    # check if the player already has the specific item in their inventory

    def __str__(self):
        return f'''
        Username: {self.username}
        Name: {self.name}
        HP: {self.hp}
        Power: {self.power}
        Gender: {self.gender}
        Armour: {self.armour}
        Inventory: {self.inventory}
        Weapon: {self.weapon}
        Current Location: {self.current_location}
        Floor Access: {self.floor_access}
        '''




class FloorGuardian(Character):
    # This class creates Floor Guardians

    def __init__(self, name="Default Monster", type="monster", description="", level=1):
        super().__init__(name, type)
        self.description = description
        self.level = level
        self.hp = 10 ** (level / 20) + 3 * level
        self.power = 2 ** (level / 6.2) + 3 * level
        self.set_name()

    def set_name(self):
        self.name = f"Level {self.level} {self.type.capitalize()}"

    # def die(self, enemy):


    def __str__(self):
        return f'''
        Name: {self.name}
        Type: {self.type}
        Level: {self.level}
        Description: {self.description}
        HP: {self.hp}
        Power: {self.power}
        Gender: {self.gender}
        '''


inventory = {
    "weapon": [
        {"id": "weSword100", "type": "weapon", "name": "Sword", "power": 100},
        {
            "id": "weBaseballBat15",
            "type": "weapon",
            "name": "Baseball Bat",
            "power": 15,
        },
    ],
    "armour": [
        {
            "id": "arMetalHelmet50",
            "type": "armour",
            "name": "Metal Helmet",
            "defence": 50,
        },
        {"id": "arVest70", "type": "armour", "name": "Vest", "defence": 70},
    ],
    "potions": [
        {
            "id": "poHealthPotion100",
            "type": "potion",
            "name": "Health Potion",
            "heal": 100,
        }
    ],
}

thomas = Player("bigboy69", "thomas", "ADC")
rabbit = FloorGuardian("rabbit", "animal", level=1)

print(thomas)
print(rabbit)
# print(thomas.weapon)
thomas.take_damage(rabbit.power, rabbit)
thomas.deal_damage(rabbit)

# print(thomas.weapon)
