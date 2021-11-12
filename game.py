from characters import Player


def introduction():
    print(
        """

    Welcome to the Tower of Greed! A place where only the strong will survive,
    and only the strongest will be able to get out of...

    You are a prisoner in this tower 
    with 100 floors in the middle of the ocean. At each floor there is 
    a monster guarding the level. You can only advance to the next floor 
    if you or your team beats the monster. The only way out of the 
    prison is to be the first person to beat the monster at 100th floor 
    and take the helicopter out.

    """
    )


def create_character():
    # could include a feature to rollback selections or exit

    player_name = input("What is your name?")
    user_gender = ""

    while user_gender != "m" and user_gender != "f":
        user_gender = input(
            "What is your gender? (type M for Male and F for Female):"
        ).lower()

    print("What type of character do you want to be?")
    print(
        """
    1. Balanced: balanced health points and hitpoints
    2. Tank: low hitpoints but very high health
    3. ADC: very high hitpoints but low health
    """
    )
    user_input = ""
    user_type = ""
    while user_input != "1" and user_input != "2" and user_input != "3":
        user_input = input("Please select 1, 2, or 3: ")

    if user_input == "1":
        user_type = "Balanced"
    elif user_input == "2":
        user_type = "Tank"
    else:
        user_type = "ADC"

    player = Player(player_name, user_type, user_gender)

    # temp = vars(player)
    # for item in temp:
    #     print(item, ":", temp[item])

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


create_character()
