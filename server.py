# pyzChat-Server
import zmq

class Chatroom:
    def __init__(self, name, host) -> None:
        self.name = name
        self.host = host
        self.party = []

    def join(self):
        pass

chatrooms = ['lion', 'tiger', 'leopard']

def main():
    context = zmq.Context()
    print("pyzChat Server activated...")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")
    while True:
        request = socket.recv_string()
        if request[0] == "#":
            if request[:8] == "#setuser":
                name = request.split()[1]
                new_user = {"name": name, "id": 1234}
                # Add new_user in DB
                # if adding succeed:
                socket.send_json(new_user)
            elif request == "#chatrooms":
                rooms_str = '\n'.join(chatrooms)
                socket.send_string(rooms_str)
            elif request[:8] == "#addroom":
                room_name = request.split()[1]
                chatrooms.append(room_name)
                rooms_str = '\n'.join(chatrooms)
                socket.send_string(rooms_str)
        else:
            socket.send_string(f"{request} wow")


if __name__ == '__main__':
    main()


