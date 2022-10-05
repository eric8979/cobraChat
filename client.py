# pyzChat-Client
import random
import time
import zmq
import sys

def main(argv):
    context = zmq.Context()
    print("Connecting to pyzChat server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")

    while True:
        requestMsg = input('command : ')
        # SHOW chatrooms
        if (requestMsg[:3] == "#re") or (requestMsg == "#chatrooms"):
            socket.send_string("#chatrooms")
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")
        # ADD chatroom
        elif requestMsg == "#addroom":
            room_name = input("Room name(no spaces) : ")
            socket.send_string("#addroom " + room_name)
            reply = socket.recv_string()
            print(f"chatroom list : \n{reply}")

        elif requestMsg == "quit":
            print("Exit pyzChat...")
            break


if __name__ == '__main__':
    # while True:
    #     print("LOGO")
    #     print("Welcome to pyzchat!")
    #     print("Enter `#refresh` or `#re` if you don't see a room you want to join, Enter `#help` for any other help.")
    #     print("<Chatrooms>")
    #     break
    main(sys.argv)

