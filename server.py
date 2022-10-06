# pyzChat-Server
import zmq

class Chatroom:
    def __init__(self, name, host) -> None:
        self.name = name
        self.host = host
        self.party = []

    def join(self):
        pass

class User:
    def __init__(self, name) -> None:
        self.name = name
        self.id = "345r34e34"    # TODO
        self.pwd = "1234"

tom = User("tom")
eric = User("eric")
joe = User("joe")

users = [tom, eric, joe]
username = {tom.name, eric.name, joe.name}
userpwd = {tom.pwd, eric.pwd, joe.pwd}
chatrooms = ['lion', 'tiger', 'leopard']

def main():
    context = zmq.Context()
    print("pyzChat Server activated...")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")
    while True:
        request = socket.recv_string()

        if request[:6] == "#login":
            login_info = request.split()
            id = login_info[1]
            pwd = login_info[2]
            if id in username and pwd in userpwd:
                # Grant Access
                pass
                
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


# TODO: use django?(web-framework for chatrooms and zmq for a chatroom?)
