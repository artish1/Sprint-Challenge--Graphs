

class Graph:

    def __init__(self):
        self.rooms = {}
        self.opposite_directions = {
            'n': 's',
            's': 'n',
            'e': 'w',
            'w': 'e'
        }

    def add_room(self, room):
        if not room.id in self.rooms:
            room_info = {}
            for direction in room.get_exits():
                room_info[direction] = "?"
            self.rooms[room.id] = room_info

    def connect_room(self, from_room, to_room, direction):
        if self.rooms[from_room.id] is None:
            return print("Cannot connect a room that has not been added to the group initially")
        
        if self.rooms[from_room.id][direction] is None:
            return print(f"Room {from_room.id} does not have a {direction} direction!")
        
        self.rooms[from_room.id][direction] = to_room.id
        opposite_dir = self.opposite_directions[direction]
        self.rooms[to_room.id][opposite_dir] = from_room.id

    def is_unexplored(self, room, direction):
        return self.rooms[room.id][direction] == '?'

    def print_rooms(self):
        print(self.rooms)

    