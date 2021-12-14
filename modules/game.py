from modules.characters import Player
import modules.user_accounts as user_accounts
import time
from modules.save_load import load_player



# Welcome screen
def welcome_screen():
# ART source: https://patorjk.com/software/taag/#p=testall&f=4Max&t=WELCOME%20TO%20THE%20%0ATOWER%20OF%20GREED
    print('''     
                         ▀                                                                                                                                          
    ███      ▄██████▄   ▄█     █▄     ▄████████    ▄████████       ▄██████▄     ▄████████         ▄██████▄     ▄████████    ▄████████    ▄████████ ████████▄        
▀█████████▄ ███    ███ ███     ███   ███    ███   ███    ███      ███    ███   ███    ███        ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███       
   ▀███▀▀██ ███    ███ ███     ███   ███    █▀    ███    ███      ███    ███   ███    █▀         ███    █▀    ███    ███   ███    █▀    ███    █▀  ███    ███       
    ███   ▀ ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄▄██▀      ███    ███  ▄███▄▄▄           ▄███         ▄███▄▄▄▄██▀  ▄███▄▄▄      ▄███▄▄▄     ███    ███       
    ███     ███    ███ ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ███    ███ ▀▀███▀▀▀          ▀▀███ ████▄  ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀▀███▀▀▀     ███    ███       
    ███     ███    ███ ███     ███   ███    █▄  ▀███████████      ███    ███   ███               ███    ███ ▀███████████   ███    █▄    ███    █▄  ███    ███       
    ███     ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███      ███    ███   ███               ███    ███   ███    ███   ███    ███   ███    ███ ███   ▄███       
   ▄████▀    ▀██████▀   ▀███▀███▀    ██████████   ███    ███       ▀██████▀    ███               ████████▀    ███    ███   ██████████   ██████████ ████████▀        
                                                  ███    ███                                                  ███    ███                                      
                                                  
                                                
''')


# the login screen returns player object
def login_screen():
    print(
        """
    Would you like to 
    1. Login
    2. Create an account
    """
    )
    user_input = ""
    while user_input != "1" and user_input != "2":
        user_input = input("Please select 1 or 2: ")

    if user_input == "1":
        username = user_accounts.login()
        time.sleep(0.5)
        print("Loading game...")
        # time.sleep(1)
        player = load_player(username)
        return player

    else:
        # account creation procedure returns the player's username
        username = user_accounts.create_account()
        introduction()
        time.sleep(2)
        player = create_character(username)
        return player



def introduction():

    print(''' 
    Welcome to the Tower of Greed! A place where only the strong will survive,
    and only the strongest will be able to get out of...''')

    time.sleep(1)

    # Ascii art source: https://www.asciiart.eu/buildings-and-places/castles
    print(
        """


                                                |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       \,/
                                             ||: , |            /`\

                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~


    You are a prisoner in this tower with 100 floors in the middle of the ocean. 
    At each floor there is  a monster guarding the level. You can only advance 
    to the next floor if you or your team beats the monster. The only way out 
    of the prison is to be the first person to beat the monster at 100th floor 
    and take the helicopter out.

    """
    )


# the create character function takes a username as a parameter, creates a character, and returns the character
def create_character(username):
    player_name = input("What is your name? ")
    user_gender = ""

    # ask for the user's gender
    while user_gender != "m" and user_gender != "f":
        user_gender = input(
            "What is your gender? (type M for Male and F for Female):"
        ).lower()

    # ask the user what type of character they want to be
    print("What type of character do you want to be?")
    print(
        """
    1. Balanced: balanced health points and power
    2. Tank: low power but very high health
    3. ADC: very high power but low health
    """
    )
    user_input = ""
    user_type = ""
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = input("Please select 1, 2, or 3: ")

    #set player type
    if user_input == "1":
        user_type = "Balanced"
    elif user_input == "2":
        user_type = "Tank"
    else:
        user_type = "ADC"

    # create a Player instance using the information provided by the user
    player = Player(username, player_name, user_type, user_gender)

    # temp = vars(player)
    # for item in temp:
    #     print(item, ":", temp[item])
    print("Character created successfully")
    return player


def win_message():
    print(
        """

    You have thrived and became the strongest in this world of greed. 
    Yet, you have chosen to leave your position of power and status in 
    this world for true freedom. You understand the value of freedom. 
    You are now free!

    """
    )
