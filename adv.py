from room import Room
from player import Player
from world import World
from graph import Graph

import random
from ast import literal_eval

# Functions to organize code
def get_unexplored_directions(room):
    unexplored_directions = []
    for direction in room.get_exits():
        if graph.is_unexplored(room, direction):
            unexplored_directions.append(direction)
    return unexplored_directions


# Made to a function for readability later on
def get_random_direction(direction_list):
    return direction_list[random.randint(0, len(direction_list) - 1)]


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Graph
graph = Graph()
graph.add_room(player.current_room)


# prev_room = player.current_room
# player.travel("n")
# graph.add_room(player.current_room)
# graph.connect_room(prev_room, player.current_room, "n")

# graph.print_rooms()

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

finished = False
while not finished:
    # Pick random unexplored direction from player's current room.
    unexplored_directions = get_unexplored_directions(player.current_room)
    # (Base Case ?) If room has no unexplored paths, walk back to nearest room that does contain an unexplored (?) path.
    # BFS ^
    if len(unexplored_directions) == 0:
        # TODO BFS to nearest room that has unexplored paths

        # TODO If BFS cannot find a room that has unexplored paths, it's done.
        finished = True  # TODO Temporary
    else:
        # Get random unexplored direction
        random_direction = get_random_direction(unexplored_directions)

        # Preserve previous room to track connections
        prev_room = player.current_room
        # Travel
        player.travel(random_direction)

        graph.add_room(player.current_room)
        graph.connect_room(prev_room, player.current_room, random_direction)
        # Log direction
        traversal_path.append(random_direction)


graph.print_rooms()
print(traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited"
    )
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
