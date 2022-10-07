# pyzChat-Client
import zmq
from intro import intro
from help import help

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    name = intro() # Print intro msg & ask for username
    if name == "quit":
        print("Bye Bye~")
        return

    my_info = {"userid" : 1234, "username" : name}
    print("Your name/id are all set!\n")
    print("---------------------------------------")
    print(f"username : {my_info['username']}")
    print(f"userid : {my_info['userid']}")
    print("---------------------------------------")
    print("Tip : Type `#help` for every(5) commands.")

    # Show chatroom right after user logs in.
    socket.send_string("#chatrooms")
    print(socket.recv_string())

    while True:
        message = input(">>> ")
        if message == "#quit":
            print("Exit pyzChat...")
            break
        # HELP
        if message == "#help":
            help()
        # SHOW chatrooms
        elif (message[:3] == "#re") or (message == "#chatrooms"):
            socket.send_string("#chatrooms")
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")
        # ADD chatroom
        elif message == "#addroom":
            room_name = input("Room name(no spaces) : ")
            socket.send_string("#addroom " + room_name)
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")
        # ENTER chatroom
        elif message == "#enterroom":
            room_name = input("Room name : ")
            print(f"Entering the room {room_name}")
            # Enter the room


if __name__ == '__main__':
    main()

