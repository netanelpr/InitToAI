import pandas as pd
import heapq

class PrioreyQueue:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, data):
        heapq.heappush(self.heap, data)
        self.size =+ 1

    def pop(self):
        self.size =- 1
        return heapq.heappop(self.heap)

    def empty(self):
        return self.size == 0

# The function initializes and returns open
def init_open():
    return PrioreyQueue()

# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    open_list.insert(s)

# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    return open_list.pop()

# The function returns neighboring locations of s_location
def get_neighbors(grid, s_location):
    neighbors = []
    currentX = s_location[0]
    currentY = s_location[1]
    gridSize = len(grid)
    
    if(currentX < gridSize - 1):
        neighbors.append((currentX + 1, currentY))
    if(currentX > 0):
        neighbors.append((currentX -1, currentY))

    if(currentY < gridSize - 1):
        neighbors.append((currentX, currentY + 1))
    if(currentY > 0):
        neighbors.append((currentX, currentY - 1))

    for neigbor in neighbors:
        if(grid[neigbor[0], neigbor[1]] == '@'):
            neighbors.remove(neigbor)

    return neighbors

# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    return s_location[0] == goal_location[0] and s_location[1] == goal_location[1]

# The function estimates the cost to get from s_location to goal_location
def calculate_heuristic(s_location, goal_location):
    return abs(s_location[0] - goal_location[0]) + \
        abs(s_location[0] - goal_location[0])

# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, g, h, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, False)
    start = (0, 0, 0, start_location[0], start_location[1], False)
    open_list = init_open()
    closed_list = set()
    # Mark the source node as
    # visited and enqueue it
    insert_to_open(open_list, start)
    while not open_list.empty():
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        s_location = (s[3], s[4])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by AStar Search:", len(closed_list))
            return s
        neighbors_locations = get_neighbors(grid, s_location)
        for n_location in neighbors_locations:
            if n_location in closed_list:
                continue
            h = calculate_heuristic(n_location, goal_location)
            g = s[2] + 1
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)

def print_route(s):
    for r in s:
        print(r)

def get_route(s):
    route = []
    while s:
        s_location = (s[3], s[4])
        route.append(s_location)
        s = s[5]
    route.reverse()
    return route

def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))
