user_accounts = [
    {"username": "asdf", "user_password": "asdf"},
    {"username": "qwer", "user_password": "qwer"},
]


def create_account():
    username = ""
    user_password = ""
    username_input = input("Enter Username:")

    if not user_accounts:
        username = username_input
        print("You are our first account!")

    for i in user_accounts:

        while username_input in i["username"]:
            print("username already exists, please select another username")
            username_input = input("Enter Username:")

        else:
            username = username_input
    user_password = input("Enter Password:")
    user_account = {"username": username, "user_password": user_password}
    user_accounts.append(user_account)


def login():
    username_input = input("Enter Username:")

    for i in user_accounts:
        while username_input not in i["username"]:
            print(
                "Username not found, please enter a valid username or create a new account"
            )
            username_input = input("Enter Username:")
        else:
            print("found username")
            user_password_input = input("Enter Password:")
            tries = 3
            while user_password_input != i["user_password"]:
                tries -= 1
                if tries == 0:
                    print("You have entered an incorrect password too many times")
                    break
                print(f"Password Incorrect, you have {tries} left")
                user_password_input = input("Enter Password:")
            else:
                print("You have logged in successfully")
                break
            break


# create_account()
# create_account()
print(user_accounts)
login()
