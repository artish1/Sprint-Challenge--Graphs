from util import Queue


class Graph:
    def __init__(self):
        self.rooms = {}
        self.opposite_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

    def add_room(self, room):
        if not room.id in self.rooms:
            room_info = {}
            for direction in room.get_exits():
                room_info[direction] = "?"
            self.rooms[room.id] = room_info

    def get_neighbors(self, room_id):
        if room_id in self.rooms:
            return self.rooms[room_id]
        else:
            return None

    def connect_room(self, from_room, to_room, direction):
        if self.rooms[from_room.id] is None:
            return print(
                "Cannot connect a room that has not been added to the group initially"
            )

        if self.rooms[from_room.id][direction] is None:
            return print(f"Room {from_room.id} does not have a {direction} direction!")

        self.rooms[from_room.id][direction] = to_room.id
        opposite_dir = self.opposite_directions[direction]
        self.rooms[to_room.id][opposite_dir] = from_room.id

    def is_unexplored(self, room, direction):
        return self.rooms[room.id][direction] == "?"

    def find_room_with_unexplored(self, starting_room):
        """
        Returns a list of room id's containing the shortest path from the starting_room
        to the nearest room that has unexplored directions
        using breadth-first search 
        """
        # Create queue
        qq = Queue()
        #            path of room ids, path of directions
        qq.enqueue([[starting_room.id], []])
        visited = set()
        while qq.size() > 0:
            path = qq.dequeue()

            # Extract paths
            id_path = path[0]
            direction_path = path[1]

            # If not visited
            if id_path[-1] not in visited:
                # Detect if this room has any unexplored directions
                current_room_id = id_path[-1]
                for direction in self.rooms[current_room_id]:
                    if self.rooms[current_room_id][direction] == "?":
                        # Found a room with an unexplored direction!
                        # Return the path
                        return path

                # Mark as visited
                visited.add(current_room_id)
                # Enqueue any neighboring rooms
                for neighbor_direction in self.get_neighbors(current_room_id):
                    new_path = list(path)
                    new_direction_path = list(direction_path)
                    new_id_path = list(id_path)
                    neighbor_id = self.rooms[current_room_id][neighbor_direction]
                    # New way
                    new_id_path.append(neighbor_id)
                    new_direction_path.append(neighbor_direction)
                    new_path[0] = new_id_path
                    new_path[1] = new_direction_path

                    # Old way
                    # new_path.append(neighbor_id)
                    qq.enqueue(new_path)
        # Returning None means we did not find any room with an unexplored path
        return None

    def print_rooms(self):
        print(self.rooms)
