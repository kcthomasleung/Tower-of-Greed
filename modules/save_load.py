from modules.characters import Player
import modules.objects as obj
from rich import print

def save_player(player):

    equipped_armour_list = []
    weapon_list = []
    armour_list = []
    potion_list = []

    if player.armour:
        for item in player.armour:
            # add all the player's equipped armour into a list
            equipped_armour_list.append(item.id)

    if player.inventory["weapon"]:
        for item in player.inventory["weapon"]:
            # add all the player's inventory weapons into a list
            weapon_list.append(item.id)

    if player.inventory["armour"]:
        for item in player.inventory["armour"]:
            # add all the player's inventory armour into a list
            armour_list.append(item.id)

    if player.inventory["potion"]:
        for item in player.inventory["potion"]:
            # add all the player's inventory potion into a list
            potion_list.append(item.id)

    # turn all the lists above into a string of comma separated values
    equipped_armour_csv = ",".join(equipped_armour_list)
    weapon_csv = ",".join(weapon_list)
    armour_csv = ",".join(armour_list)
    potion_csv = ",".join(potion_list)

    # write player stats into a txt file
    try:
        # notice this relative path is relative to main.py. Will have to go up one directory if running from other module files
        with open(
            f"./saved_games/{player.username}_saved_game.txt", "w"
        ) as file_object:
            file_object.write(
                "username,name,type,hp,power,gender,weapon,current_location,floor_access \n"
                f"{player.username},{player.name},{player.type},{player.hp},{player.power},{player.gender},{player.weapon.id},{player.current_location},{player.floor_access} \n"
                f"equipped armour: {equipped_armour_csv}\n"
                "-------------inventory------------\n"
                f"weapon: {weapon_csv}\n"
                f"armour: {armour_csv}\n"
                f"potion: {potion_csv}\n"
            )

        print("your game has been saved successfully")
    except FileNotFoundError:
        print("File not found")


# The load player function either returns the player object or FileNotFoundError if the saved file cannot be found
def load_player(username):
    try:
        # notice this relative path is relative to main.py. Will have to go up one directory if running from other module files
        with open(f"./saved_games/{username}_saved_game.txt") as file_object:

            lines = file_object.readlines()

            # create list variable for a list of comma seperated player attributes
            player_attrib_list = lines[1].strip().split(",")

            # assign player attributes to variables
            player_username = player_attrib_list[0]
            player_name = player_attrib_list[1]
            player_type = player_attrib_list[2]
            player_hp = float(player_attrib_list[3])
            player_power = float(player_attrib_list[4])
            player_gender = player_attrib_list[5]
            player_weapon = player_attrib_list[6]
            player_current_location = player_attrib_list[7]
            player_floor_access = int(player_attrib_list[8])

            # create player object and set attributes
            player = Player(
                player_username, player_name, player_type, gender=player_gender
            )
            player.hp = player_hp
            player.power = player_power
            player.weapon = obj.create_item_with_id(player_weapon)
            player.current_location = player_current_location
            player.floor_access = player_floor_access

            # add equipped armour in text file into the player's equipped armour
            # check if there are any armour in the file
            equipped_armour_list = lines[2].strip().split(": ")
            if len(equipped_armour_list) == 1:
                pass
            else:
                # a string of comma separated armour ids
                equipped_armour = lines[2].strip().split(": ")[1]

                # a list of armour ids
                player_equipped_armour = equipped_armour.split(",")

                # add armour into player armour list using item ids
                for item in player_equipped_armour:
                    armour = obj.create_item_with_id(item)
                    player.armour.append(armour)

            # add items to inventory
            # check if there are any items in the inventory section of the file
            inventory_weapons_list = lines[4].strip().split(": ")
            if len(inventory_weapons_list) == 1:
                pass
            else:
                # if the text file contains weapons in the inventory, do this
                # a string of comma separated inventory weapon ids
                inventory_weapons = lines[4].strip().split(": ")[1]

                # a list of inventory weapon ids
                player_inventory_weapons = inventory_weapons.split(",")
                # add weapons into player inventory
                for item in player_inventory_weapons:
                    weapon = obj.create_item_with_id(item)
                    player.inventory["weapon"].append(weapon)

            # same for armour and potion
            inventory_armour_list = lines[5].strip().split(": ")
            if len(inventory_armour_list) == 1:
                pass
            else:
                inventory_armour = lines[5].strip().split(": ")[1]

                player_inventory_armour = inventory_armour.split(",")
                for item in player_inventory_armour:
                    armour = obj.create_item_with_id(item)
                    player.inventory["armour"].append(armour)

            inventory_potion_list = lines[6].strip().split(": ")
            if len(inventory_potion_list) == 1:
                pass
            else:
                inventory_potion = lines[6].strip().split(": ")[1]
                player_inventory_potion = inventory_potion.split(",")
                for item in player_inventory_potion:
                    potion = obj.create_item_with_id(item)
                    player.inventory["potion"].append(potion)

        return player

    except FileNotFoundError:
        print(
            "No saved game file found for this account. Try logging in to another account or start a new game"
        )
