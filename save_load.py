from characters import Player
import objects as obj

thomas = Player("bigboy69", "Thomas", "ADC")

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
print(thomas)

def save_player():
    
    equipped_armour_list = []
    weapon_list = []
    armour_list = []
    potion_list = []

    for item in thomas.armour:
        equipped_armour_list.append(item.id)

    for item in thomas.inventory["weapon"]:
        weapon_list.append(item.id)

    for item in thomas.inventory["armour"]:
        armour_list.append(item.id)

    for item in thomas.inventory["potion"]:
        potion_list.append(item.id)

    equipped_armour_csv = ",".join(equipped_armour_list)
    weapon_csv = ",".join(weapon_list)
    armour_csv = ",".join(armour_list)
    potion_csv = ",".join(potion_list)


    # write player stats into a txt file
    try:
        with open(f"saved_games/{thomas.username}_saved_game.txt", "w") as file_object:
            file_object.write(
                "username,name,type,hp,power,gender,weapon,current_location,floor_access \n"
                f"{thomas.username},{thomas.name},{thomas.type},{thomas.hp},{thomas.power},{thomas.gender},{thomas.weapon.id},{thomas.current_location},{thomas.floor_access} \n"
                f"equipped armour: {equipped_armour_csv}\n"
                "-------------inventory------------\n"
                f"weapon: {weapon_csv}\n"
                f"armour: {armour_csv}\n"
                f"potion: {potion_csv}\n"
            )

    except FileNotFoundError:
        print("File not found")

save_player()


def load_player():
    try:
        with open(f"saved_games/{thomas.username}_saved_game.txt") as file_object:

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
            player = Player(player_username, player_name, player_type, gender=player_gender)
            player.hp = player_hp
            player.power = player_power
            player.weapon = obj.create_item_with_id(player_weapon)
            player.current_location = player_current_location
            player.floor_access = player_floor_access

            # a string of comma separated armour ids
            equipped_armour = lines[2].strip().split(": ")[1] 

            # a list of armour ids
            player_equipped_armour = equipped_armour.split(",")

            # add armour into player armour list using item ids
            for item in player_equipped_armour:
                armour = obj.create_item_with_id(item)
                player.armour.append(armour)

            # add items to inventory
            # a string of comma separated inventory weapon ids
            inventory_weapons = lines[4].strip().split(": ")[1]
            # a list of inventory weapon ids
            player_inventory_weapons = inventory_weapons.split(",")
            # add weapons into player inventory
            for item in player_inventory_weapons:
                weapon = obj.create_item_with_id(item)
                player.inventory["weapon"].append(weapon)

            # same for armour and potion
            inventory_armour = lines[5].strip().split(": ")[1]
            player_inventory_armour = inventory_armour.split(",")
            for item in player_inventory_armour:
                armour = obj.create_item_with_id(item)
                player.inventory["armour"].append(armour)

            inventory_potions = lines[6].strip().split(": ")[1]
            player_inventory_potions = inventory_potions.split(",")
            for item in player_inventory_potions:
                potion = obj.create_item_with_id(item)
                player.inventory["potion"].append(potion)
            
        return player

    except FileNotFoundError:
        print("File not found")



print(load_player())