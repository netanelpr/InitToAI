import numpy
import a_star_search as astar
import breadth_first_search as bfs
from route_grid import create_grid
import time
import copy

ROUTE_LEN_1 = 39
ROUTE_LEN_2 = 291

def grid_test(test_num=1, print_route=False):
    grid, start_location, end_location = create_grid(test_num)
    print(numpy.shape(grid))
    print("--- AStar solver ---")
    start_time = time.time()
    s_astar = astar.astar_search(grid, start_location, end_location)
    a_route = astar.get_route(s_astar)
    print("Route length:", len(a_route))
    tot1 = round(time.time() - start_time, 4)
    print("Running time:", tot1)
    if print_route:
        print("AStar route: ")
        astar.print_grid_route(a_route, copy.copy(grid))

    print("--- BFS solver ---")
    start_time = time.time()
    s_bfs = bfs.bfs(grid, start_location, end_location)
    b_route = bfs.get_route(s_bfs)
    tot2 = round(time.time() - start_time, 4)
    print("Running tim:", tot2)
    print("Route length:", len(b_route))
    if print_route:
        print("BFS route: ")
        bfs.print_grid_route(b_route, copy.copy(grid))

    # except:
    #     return False
    # print(len(b_route), len(a_route), tot1, tot2)
    if len(b_route) == len(a_route):
        if test_num == 1:
            if len(b_route) == ROUTE_LEN_1:
                return True
        elif test_num == 2:
            if len(b_route) == ROUTE_LEN_2:
                if tot1 < tot2:
                    return True
                else:
                    print("Running time is too high for AStar search")
                    return False
    return False

print("------------------ Test 1 ------------------")
print("Testing the search algorithms on first problem instance (running time may not be better for AStar Search):")
# If you don't want to print the route, you may change print_route to False
sanity = grid_test(1, print_route=True)
print("First problem instance passed? ", sanity)

print("------------------ Test 2 ------------------")
print("Testing the search algorithms on the second problem instance (running time should be better for AStar Search):")
sanity = grid_test(2)
print("Second problem instance passed? ", sanity)
