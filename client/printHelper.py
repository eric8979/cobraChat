def printIntro():
    print("""
                          ____ _           _
         _ __  _   _ ____/ ___| |__   __ _| |_
        | '_ \| | | |_  / |   | '_ \ / _` | __|
        | |_) | |_| |/ /| |___| | | | (_| | |_
        | .__/ \__, /___|\____|_| |_|\__,_|\__|
        |_|    |___/
    """)
    print("Welcome to pyzChat! Your Simple, Fast and Secure chatting app")

    print("\nFirst set your username to identify you in a chatroom.")
    print("Type `quit` if you want to quit.")
    username = input("username : ")
    return username


def printHelp():
    print("""\n
---------------- pyzChat Help -------------------

1. Commands
    1-1. Chatrooms
        #chatrooms : Show existing chatrooms

        #refresh / #re : Refresh chatrooms

        #addroom : Create a room (App will ask for the Room's name)

        #enterroom : Enter a chatroom. (App will ask for the Room's name)

    1-2. Quit
        #quit : quit pyzChat

-------------------------------------------------\n
    """)


def printUser(user_info):
    print(f"""
-------------------------------------------------
username : {user_info['username']}

userid : {user_info['userid']}
-------------------------------------------------
Tip : Type `#help` for every(5) commands.
    """)


def printRooms(rooms_info):
    print(f"""
---------------- pyz Chatrooms -------------------

{rooms_info}
-------------------------------------------------
    """)
