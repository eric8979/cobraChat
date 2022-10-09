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
lion = Chatroom("lion")
tiger = Chatroom("tiger")
leopard = Chatroom("leopard")
chatrooms = [lion, tiger, leopard]

def main():
    context = zmq.Context()
    print("pyzChat Server activated...")
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5557")

    while True:
        request = socket.recv_string()
        if request == "#chatrooms":
            rooms = []
            for i in range(len(chatrooms)):
                room = f"{i+1}. {chatrooms[i].name} (👨‍👩‍👦‍👦 {len(chatrooms[i].party)}) - ID : {chatrooms[i].id}\n"
                rooms.append(room)
            socket.send_string("\n".join(rooms))
        elif request[:8] == "#addroom":
            room_name = request.split()[1]
            # Create a room
            new_room = Chatroom(room_name)
            chatrooms.append(new_room)
            # Fetch rooms
            rooms = []
            for i in range(len(chatrooms)):
                room = f"{i+1}. {chatrooms[i].name} (👨‍👩‍👦‍👦 {len(chatrooms[i].party)}) - ID : {chatrooms[i].id}\n"
                rooms.append(room)
            socket.send_string("\n".join(rooms))


if __name__ == '__main__':
    main()


