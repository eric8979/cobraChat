# pyzChat-Client
import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    print("Welcome to pyzChat!")
    username = input("Set your username : ")
    socket.send_string(f"#setuser {username}")
    user = socket.recv_json()
    print(user)
    while True:
        print("Enter #help for commands")
        message = input(">>> ")
        if message[0] == "#":
            if message == "#quit":
                print("Exit pyzChat...")
                break
            commands(socket, message)
        else:
            socket.send_string(message)
            reply = socket.recv_string()
            print(reply)

def commands(socket, message):
        # HELP
        if message == "#help":
            print("Enter #chatrooms for chatrooms")
            print("Enter #refresh or #re to refresh chatrooms")
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
        elif message == "#removeroom":
            room_name = input("Room name(no spaces) : ")
            # remove room only if the user is the host
        elif message == "#enterroom":
            room_name = input("Room name : ")
            print(f"Entering the room {room_name}")
            # enter the room


if __name__ == '__main__':
    main()

