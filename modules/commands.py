import time
from modules.save_load import save_player
import modules.characters as characters
import modules.tower as tower


def help():
    print(
        """
    Available commands:

        inventory: check your inventory
        level: check you current floor level
        location: check your current location
        battle: battle the floor guardian of your current level
        look: have a look at what is around you
        health: check your health points
        who: display all the users in the room
        stats: display game statistics and map of current location
        save: save your current game progress
        exit: exit the game
        
    
    """
    )


def stats(player):
    print(player)


def battle(player, tower):
    # this command is to initiate a battle between the player and a floor guardian
    # set player room and level variables
    player_room = player.current_location[-1]
    player_level = int("".join(filter(lambda i: i.isdigit(), player.current_location)))
    # assign monster object to variable from the tower object passed into the function
    monster = tower.floors[player_level - 1].battle_room.floor_guardian

    # check if the player is currently in a battle room
    if "b" not in player.current_location:
        # if the player is not in a battle room, set their location to the battle room of the same level
        player.current_location = f"{player_level}b"
        print(f"You have entered the the battle room of floor {player_level}")
        user_response = input("Would you like to battle the Floor Guardian?").lower()

        while user_response != "yes" and user_response != "no":
            print("Please enter yes/no")
            user_response = input(
                "Would you like to battle the Floor Guardian?"
            ).lower()
        if user_response == "yes":
            # player confirms they would like to battle the floor guardian --> loops attack methods until one party dies
            while (
                monster.hp > 0
                and player.hp > 0
                and player.current_location == f"{player_level}b"
            ):
                player.attack(monster)
                # check if the player has already defeated the monster (if defeated, player will be at the next level)
                if player.current_location == f"{player_level}b":
                    # player location is still the same meaning the player has not yet defeated the monster
                    monster.attack(player)
                time.sleep(1.5)

        elif user_response == "no":
            pass

    else:
        player.attack(tower.floors[player_level].battle_room.floor_guardian)


def location(player):
    # This command displays the player's current location
    # Set player floor level using the player current_location attribute
    player_level = int("".join(filter(lambda i: i.isdigit(), player.current_location)))

    # Set player room using the current_location attribute
    player_room = ""
    if player.current_location[-1] == "a":
        player_room = "Lobby"
    elif player.current_location[-1] == "b":
        player_room = "Battle Room"
    else:
        print("Error: current_location does not contain 'a' or 'b'")

    print(f"Your current location is: Level {player_level} {player_room}")


def save(player):
    save_player(player)


# def inventory(player):


# def map()

# def change_gender()


# tower = tower.Tower()
# player = characters.Player("bigboy69", "Thomas", "ADC")
# battle(player)
