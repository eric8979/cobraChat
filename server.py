# pyzChat-Server
import zmq

chatrooms = ['lion', 'tiger', 'leopard']

def main():
    context = zmq.Context()
    print("pyzChat Server activated...")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")

    while True:
        request = socket.recv_string()

        if request == "#chatrooms":
            rooms_str = '\n'.join(chatrooms)
            socket.send_string(rooms_str)
        elif request[:8] == "#addroom":
            room_name = request.split()[1]
            chatrooms.append(room_name)
            rooms_str = '\n'.join(chatrooms)
            socket.send_string(rooms_str)


# Boilerplate code that protects users from accidentally invoking the script.
if __name__ == '__main__':
    main()


# TODO: use django?(web-framework for chatrooms and zmq for a chatroom?)



# Learning Note

# ZMQ doesn't know anything about the data you send except its size in bytes.
# Need formatting data before sending

# problem -> check the version(it could be fixed in a later version)
# How to check ver.
# import zmq
#
# print(f"Current libzmq version is {zmq.zmq_version()}")
# print(f"Current  pyzmq version is {zmq.__version__}")
