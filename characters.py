class Character:
    # This class is to create game characters (e.g. player and monsters)

    def __init__(self, name, type="balanced", gender="M"):
        self.name = name
        self.type = type
        self.hp = int
        self.hitpoint = int
        self.gender = gender

    # def hp_regen():
    # def deal_damage():
    # def take_damage():
    # def die():


class Player(Character):
    # This class creates a character for the player

    def __init__(
        self,
        name,
        type="balanced",
        gender="M",
    ):
        super().__init__(name, type, gender)
        self.inventory = {
            "weapon": [
                {"type": "weapon", "name": "Sword", "amount": 1, "hitpoint": 100},
                {"type": "weapon", "name": "Baseball Bat", "amount": 1, "hitpoint": 50},
            ],
            "armour": [
                {"type": "armour", "name": "Metal Helmet", "amount": 1, "defence": 50},
                {"type": "armour", "name": "vest", "amount": 1, "defence": 70},
            ],
            "potions": [{"type": "potion", "name": "Health Potion", "amount": 1}],
        }
        self.weapon = {}
        self.armour = [
            {"type": "armour", "name": "Metal Helmet", "defence": 50},
            {"type": "armour", "name": "vest", "defence": 70},
        ]
        self.current_location = "1a"
        self.floor_access = 1
        self.in_lobby = True
        self.initial_hp()

    def initial_hp(self):
        # This function takes the player type and determins their initial hp

        if self.type == "Balanced":
            self.hp = 100
            self.hitpoint = 5
        elif self.type == "ADC":
            self.hp = 50
            self.hitpoint = 10
        elif self.type == "Tank":
            self.hp = 150
            self.hitpoint = 2
        else:
            print("Error: Invalid type")

    def total_armour(self):
        # This function calculates the total armour of the player
        total = 0
        for i in range(len(self.armour)):
            total += self.armour[i]["defence"]
        return total

    def equip_weapon(self, weapon_name):
        # check if the player actually have the specified item in their inventory
        if not any(item["name"] == weapon_name for item in self.inventory["weapon"]):
            print("You do not have this item")

        else:
            # assign temp var for the weapon object from the player's inventory
            weapon = next(
                item
                for item in thomas.inventory["weapon"]
                if item["name"] == weapon_name
            )
            # only one weapon allowed to be equipped at one time. Notify user the equiped weapon will be replaced if they have a weapon already equiped
            if self.weapon:
                print(
                    "You already have a weapon equipped, it is now replaced with your selected item"
                )
                self.weapon = weapon
            else:
                self.weapon = weapon

    # def equip_armour(self, armour_name):
    # def add_to_inventory(self, item):
    #    # check if the player already has the specific item in their inventory


class FloorGuardian(Character):
    # This class creates Floor Guardians

    def __init__(self, name, type, description="", level=1):
        super().__init__(name, type)
        self.description = description
        self.level = level
        self.hp = 2 ** level
        self.hitpoint = 1 ** level


# rabbit = FloorGuardian("rabbit", "animal", level=50)
# print(rabbit.hp, rabbit.name)


# inventory = {
#     "weapon": [
#         {"type": "weapon", "name": "Sword", "amount": 1, "hitpoint": 100},
#         {"type": "weapon", "name": "Baseball Bat", "amount": 1, "hitpoint": 50},
#     ],
#     "armour": [
#         {"type": "armour", "name": "Metal Helmet", "amount": 1, "defence": 50},
#         {"type": "armour", "name": "vest", "amount": 1, "defence": 70},
#     ],
#     "potions": [{"type": "potion", "name": "Health Potion", "amount": 1}],
# }

# thomas = Player("thomas", "ADC")

# # print(thomas.inventory["weapon"])
# print(thomas.weapon)
# thomas.equip_weapon("Baseball Bat")
# print(thomas.weapon)
