# pyzChat-Client
import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    print("Welcome to pyzChat!")
    print(">>> Login")
    for i in range(3):
        id = input("user id: ")
        pwd = input("password: ")
        socket.send_string(f"#login {id} {pwd}")
        status = socket_recv_string()

    print("Enter #help for commands")
    while True:
        requestMsg = input('Command : ')
        if requestMsg == "#help":
            print("Enter #chatrooms for chatrooms")
            print("Enter #refresh or #re to refresh chatrooms")


        # Chatroom related funcitons
        # SHOW chatrooms
        elif (requestMsg[:3] == "#re") or (requestMsg == "#chatrooms"):
            socket.send_string("#chatrooms")
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")
        # ADD chatroom
        elif requestMsg == "#addroom":
            room_name = input("Room name(no spaces) : ")
            socket.send_string("#addroom " + room_name)
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")
        elif requestMsg == "#removeroom":
            room_name = input("Room name(no spaces) : ")
            # remove room only if the user is the host

        elif requestMsg == "#enterroom":
            room_name = input("Room name : ")
            print(f"Entering the room {room_name}")
            # enter the room
            
        elif requestMsg == "#quit":
            print("Exit pyzChat...")
            break


if __name__ == '__main__':
    # while True:
    #     print("LOGO")
    #     print("Welcome to pyzchat!")
    #     print("Enter `#refresh` or `#re` if you don't see a room you want to join, Enter `#help` for any other help.")
    #     print("<Chatrooms>")
    #     break
    main()

