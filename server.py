# pyzChat-Server
import zmq

class Chatroom:
    def __init__(self, name) -> None:
        self.name = name
        self.id = 1
        self.party = []

    def join(self):
        pass


# Fake chatrooms data
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


if __name__ == '__main__':
    main()


