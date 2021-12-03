

user_accounts = [
    {"username": "asdf", "user_password": "asdf"},
    {"username": "qwer", "user_password": "qwer"},
    {"username": "bigboy69", "user_password": "asdf"},
    {"username": "zxcv", "user_password": "zxcv"}
]

# create account function returns the username of the account created
def create_account():
    username = ""
    user_password = ""

    # ask for a username from the user
    username_input = input("Enter Username:")

    #check if the username input by the user already exists
    if not user_accounts:
        username = username_input
        print("You are our first account!")

    for i in user_accounts:
        # loop through user_accounts for duplicates
        while username_input in i["username"]:
            # when duplicate is found, user told to enter a different username
            print("username already exists, please select another username")
            username_input = input("Enter Username:")
        else:
            # accept the username if the username is not in our records
            username = username_input

    # ask user for a password
    user_password = input("Enter Password:")
    user_account_info = {"username": username, "user_password": user_password}

    # add user account details into a dictionary
    user_accounts.append(user_account_info)

    return user_account_info["username"]

# login function returns the username
def login():
    username_input = input("Enter Username:")
    username_exists = False

    i = 0
    for account in user_accounts:
        if username_input == account['username']:
            username_exists = True
            break
        i += 1

    if username_exists == False:
        print(
            "Username not found, please enter a valid username or create a new account"
        )

    elif username_exists == True:
        print("found username")
        user_password_input = input("Enter Password:")
        tries = 3
        while user_password_input != user_accounts[i]["user_password"]:
            tries -= 1
            if tries == 0:
                print("You have entered an incorrect password too many times")
                break
            print(f"Password Incorrect, you have {tries} left")
            user_password_input = input("Enter Password:")
        else:
            print("You have logged in successfully")

        return username_input



# create_account()
# create_account()
# print(user_accounts)
# login()
