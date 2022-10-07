def intro():
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

