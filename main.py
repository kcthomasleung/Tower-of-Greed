import modules.game as game
import modules.tower as tower
import modules.commands as commands



if __name__ == "__main__":
    game.welcome_screen()
    player = game.login_screen()
    tower = tower.Tower()

    print(
        """
    Game loaded successfully, please input commands.
    (type help to see a list of commands available)"""
    )

    while True:
        user_input = input().lower()

        if user_input == "exit":
            print("Would you like to save game before you leave? (y/n)")
            response = input()
            if response == "n":
                break
            elif response == "y":
                commands.save(player)
                break

        elif user_input == "stats":
            commands.stats(player)

        elif user_input == "help":
            commands.help()

        elif user_input == "inventory":
            commands.inventory(player)

        elif user_input == "battle":
            commands.battle(player, tower)

        elif user_input == "location":
            commands.location(player)

        elif user_input == "save":
            commands.save(player)

        elif user_input == "equip":
            commands.equip(player)

        elif user_input == "equipments":
            commands.equipments(player)

        elif user_input == "health":
            commands.health(player)

        else:
            print("Command not recognised, please type 'help' for available commands")
