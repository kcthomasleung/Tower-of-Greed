import re
import modules.objects as obj


class Character:
    # This class is to create game characters (i.e. player and monsters)

    def __init__(self, name, type="balanced", gender="M"):
        self.name = name
        self.type = type
        self.hp = float
        self.power = float
        self.gender = gender
        self.weapon = None
        self.armour = []
        self.inventory = None

    def total_power(self):
        # This function sums the weapon power and the character power and returns the character's total power
        if self.weapon:
            total_power = self.power + self.weapon.power
            return total_power

        # If the character does not have any weapons equipped, it returns the characters default power
        else:
            return self.power

    def total_armour(self):
        # This function calculates the total armour of the player
        total = 0
        for i in range(len(self.armour)):
            total += self.armour[i].defence
        return total

    def take_damage(self, damage, enemy):
        # This function handles when a character takes damage from another character
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} took {damage} damage from {enemy.name}")
            print(f"{self.name} have died")
            self.die(enemy)
        else:
            print(f"{self.name} took {damage} damage from {enemy.name}")
            print(f"{self.name}'s current health is {self.hp}")
            print("-----------------------------------------------------")

    def attack(self, enemy):
        # This method manages events when a character attacks another
        # Inspired by the lecture slides, this is to ensure we do not get negative damage
        damage = max(self.total_power() - enemy.total_armour(), 0)
        print(f"{self.name} attacks {enemy.name}")
        enemy.take_damage(damage, self)

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
            "weapon": [],
            "armour": [],
            "potion": [],
        }
        self.current_location = "1a"
        self.floor_access = 1
        self.initial_stats()

    def initial_stats(self):
        # This function takes the player type and determines their initial hp and sets their initial weapon to fists
        self.weapon = obj.Weapon("Fists", 1)

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
    def die(self, enemy):
        # parse player inventory and add every item to a list
        inventory_items = []
        for x in self.inventory:
            for item in self.inventory[x]:
                inventory_items.append(item)

        # Add the list of items into a locked loot box
        enemy.player_loot_boxes.append(
            obj.PlayerLootBox(enemy.level, inventory_items, self)
        )
        # reset player inventory, location, armour, weapon and stats
        self.inventory = {
            "weapon": [],
            "armour": [],
            "potion": [],
        }
        self.current_location = "1a"
        self.weapon = None
        self.armour = []
        self.initial_stats()

        print(
            f"You have been killed by {enemy.name}! All your inventory has been taken by {enemy.name}! Defeat {enemy.name} next time to retrieve your inventory"
        )

    def display_inventory(self):
        # method to display the player's current inventory to the player
        print(
            f"""
        Weapons: 
        """
        )

    def add_to_inventory(self, item):
        if item.type == "weapon":
            self.inventory["weapon"].append(item)
        elif item.type == "armour":
            self.inventory["armour"].append(item)
        elif item.type == "potion":
            self.inventory["potion"].append(item)
        else:
            print("Error: Item type invalid")

    def equip(self, item):
        # This function takes an item object as a parameter and adds it to the player's equipment

        # check if the player actually have the specified item in their inventory
        if (
            not any(weapon.id == item.id for weapon in self.inventory["weapon"])
            and not any(armour.id == item.id for armour in self.inventory["armour"])
            and not any(potion.id == item.id for potion in self.inventory["potion"])
        ):
            print("You do not have this item")

        else:
            # Equip weapon
            if item.type == "weapon":
                # only one weapon allowed to be equipped at one time. Notify user the equipped weapon will be replaced if
                # they have a weapon already equipped
                if self.weapon:
                    print(
                        "You already have a weapon equipped, it is now replaced with your selected item"
                    )
                    self.disarm_weapon()
                    self.weapon = item
                else:
                    self.weapon = item

            # Equip armour
            elif item.type == "armour":
                # Check if the player already has an armour for the same body part equipped
                if any(x.body_part == item.body_part for x in self.armour):
                    print(
                        f"You already have armour equipped for {item.body_part}, it is now replaced with your selected item"
                    )
                    # loop through the player's equipped armour to find the one for the same body part and replace it with the selected item
                    for i in range(len(self.armour)):
                        if self.armour[i].body_part == item.body_part:
                            return i
                    del self.armour[i]
                    self.armour.append(item)

                else:
                    # The player does not have any armour equipped for the specific body part. Simply equip selected armour
                    self.armour.append(item)

            elif item.type == "potion":
                print(
                    "You do not need to equip potions to use them. You can use them straight from your inventory"
                )

            else:
                print("Error: Invalid item type")

    def disarm_weapon(self):
        self.weapon = {}

    def disarm_armour(self, item):
        # This method loops through the player's equipped armour and finds the selected item and removes it
        i = 0
        for x in self.armour:
            if x == item:
                del self.armour[i]
                break
            i += 1
            # If the loop does not find the item specified, it notifies the user they do not have such item equipped
            print("You do not have this item equipped")

    def __str__(self):
        return f"""
    Username: {self.username}
    Name: {self.name}
    Gender: {self.gender}
    Type: {self.type}
    HP: {self.hp}
    Total Power: {self.total_power()}
    Total Defence: {self.total_armour()}
    Armour: {self.armour}
    Inventory: {self.inventory}
    Weapon: {self.weapon}
    Current Location: {self.current_location}
    Floor Access: {self.floor_access}
        """


class FloorGuardian(Character):
    # This class creates Floor Guardians

    def __init__(self, name="Default Monster", type="monster", description="", level=1):
        super().__init__(name, type)
        self.description = description
        self.level = level
        # HP and power of the Floor Guardian depends the level it is at. Grows according to a certain exponential function
        self.hp = 10 ** (level / 20) + 3 * level
        self.power = 2 ** (level / 6.2) + 3 * level
        self.loot_box = None
        self.player_loot_boxes = []
        self.set_name()
        self.set_loot_box()

    def set_name(self):
        self.name = f"Level {self.level} {self.type.capitalize()}"

    def set_loot_box(self):
        self.loot_box = obj.LootBox(self.level)

    def restore_hp(self):
        self.hp = 10 ** (self.level / 20) + 3 * self.level

    def die(self, enemy):
        # This method handles what happens when a Floor Guardian dies
        # Increase the player's floor access to the next level if the player's floor access is equal to the Floor Guardian's level
        if enemy.floor_access == self.level:
            enemy.floor_access = self.level + 1

        print(f"You have defeated {self.name}!")

        # Check if they Floor Guardian has a player_loot_box for the player that just defeated it
        for i in range(len(self.player_loot_boxes)):

            if enemy.username in self.player_loot_boxes[i].id:
                # If the Floor Guardian has a loot box that belongs to the player do this
                for item in self.player_loot_boxes[i].content:
                    # loop through the contents of the player_loot_box object and add them to the player's inventory
                    enemy.add_to_inventory(item)
                print(f"You have retrieved your lost inventory from {self.name}")

        # Reward the player with the loot box contents
        for item in self.loot_box.content:
            enemy.add_to_inventory(item)
            print(
                f"You have received {item.name} as a reward for defeating {self.name}"
            )

        # Change player location to the next level lobby
        enemy.current_location = f"{self.level + 1}a"
        print(f"You have entered level {self.level + 1} lobby")

        self.restore_hp()

    def __str__(self):
        return f"""
        Name: {self.name}
        Type: {self.type}
        Level: {self.level}
        Description: {self.description}
        HP: {self.hp}
        Power: {self.power}
        Gender: {self.gender}
        Player Loot Boxes: {self.player_loot_boxes}
        """


thomas = Player("bigboy69", "Thomas", "ADC")
rabbit = FloorGuardian("rabbit", "animal", level=1)

thomas.add_to_inventory(obj.sword)
thomas.add_to_inventory(obj.baseball_bat)
thomas.add_to_inventory(obj.metal_helmet)
thomas.add_to_inventory(obj.vest)
thomas.add_to_inventory(obj.breast_plate)
thomas.add_to_inventory(obj.gauntlet)
thomas.add_to_inventory(obj.armlet)
thomas.add_to_inventory(obj.cuisse)
thomas.add_to_inventory(obj.health_potion)

thomas.equip(obj.sword)
thomas.equip(obj.metal_helmet)
thomas.equip(obj.breast_plate)
thomas.equip(obj.gauntlet)
thomas.equip(obj.armlet)
thomas.equip(obj.cuisse)


player_loot_box1 = obj.PlayerLootBox(1, [obj.metal_helmet, obj.scarf, obj.vest], thomas)
# print(player_loot_box1)

# print(thomas.total_armour())
# print(rabbit)
# # print(thomas.weapon)
# print(thomas)

# print(rabbit)
# print(thomas)
# print(thomas.inventory)
# # rabbit.attack(thomas)
# # thomas.attack(rabbit)
# print(thomas.inventory)
