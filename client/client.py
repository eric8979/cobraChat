# pyzChat-Client
import zmq
import printHelper

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    name = printHelper.printIntro() # Print intro msg & ask for username
    if name == "quit":
        print("Bye Bye~")
        return

    my_info = {"userid" : 1234, "username" : name}
    printHelper.printUser(my_info)

    # Show chatroom right after user login.
    socket.send_string("#chatrooms")
    chatrooms = socket.recv_string()
    printHelper.printRooms(chatrooms)

    while True:
        message = input(f"<👽{my_info['username']}({my_info['userid']})> ")
        if message == "#quit":
            # erase user info?
            print("Exit pyzChat...")
            break
        # HELP
        if message == "#help":
            printHelper.printHelp()
        # SHOW chatrooms
        elif (message[:3] == "#re") or (message == "#chatrooms"):
            socket.send_string("#chatrooms")
            chatrooms = socket.recv_string()
            printHelper.printRooms(chatrooms)
        # ADD chatroom
        elif message == "#addroom":
            room_name = input("Room name(no spaces) : ")
            socket.send_string("#addroom " + room_name)
            chatrooms = socket.recv_string()
            printHelper.printRooms(chatrooms)
        # ENTER chatroom
        elif message == "#enterroom":
            room_name = input("Room name : ")
            print(f"Entering the room {room_name}...")
            # Enter the room
        else:
            print(f"Command {message} doesn't exists. Try #help to check every(5) commands.")


if __name__ == '__main__':
    main()


