import modules.game as game
from modules.save_load import save_player
import modules.tower as tower
import modules.commands as commands
from modules.characters import Player
import modules.objects as obj


if __name__ == "__main__":
    game.welcome_screen()
    player = game.login_screen()
    tower = tower.Tower()

    print(
        """
    Game loaded successfully, please input commands.
    (type help to see a list of command available)"""
    )

    while True:
        user_input = input().lower()

        if user_input == "exit":
            break

        elif user_input == "stats":
            commands.stats(player)

        elif user_input == "help":
            commands.help()

        # elif user_input == "inventory":
        #     commands.help()
        #
        elif user_input == "battle":
            commands.battle(player, tower)

        elif user_input == "location":
            commands.location(player)

        elif user_input == "save":
            commands.save(player)

        else:
            print("Command not recognised, please type 'help' for available commands")


# thomas = Player("zxcv", "zxcv", "ADC")


# thomas.add_to_inventory(obj.sword)
# thomas.add_to_inventory(obj.baseball_bat)
# thomas.add_to_inventory(obj.metal_helmet)
# thomas.add_to_inventory(obj.vest)
# thomas.add_to_inventory(obj.breast_plate)
# thomas.add_to_inventory(obj.gauntlet)
# thomas.add_to_inventory(obj.armlet)
# thomas.add_to_inventory(obj.cuisse)
# thomas.add_to_inventory(obj.health_potion)

# thomas.equip(obj.sword)
# thomas.equip(obj.metal_helmet)
# thomas.equip(obj.breast_plate)
# thomas.equip(obj.gauntlet)
# thomas.equip(obj.armlet)
# thomas.equip(obj.cuisse)

# save_player(thomas)

# commands.save(thomas)
