import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance from start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    # Manhattan distance for grid movement
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children (Adjacent squares: Up, Down, Left, Right)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for new_position in directions:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain (0 is free space, 1 is obstacle/shelf)
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            if node_position in closed_set:
                continue

            new_node = Node(node_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_node.position, end_node.position)
            new_node.f = new_node.g + new_node.h

            # Check if this path is better than one already in open list
            # (Simplified for the baseline script)
            heapq.heappush(open_list, new_node)

    return None # No path found

def print_grid(grid, path, start, goal):
    grid_copy = [row[:] for row in grid]
    for step in path:
        if step != start and step != goal:
            grid_copy[step[0]][step[1]] = "*"
    
    grid_copy[start[0]][start[1]] = "S"
    grid_copy[goal[0]][goal[1]] = "G"

    print("\nWarehouse Grid Map:")
    for row in grid_copy:
        print(" ".join(str(cell) for cell in row))
    print(f"Path Length: {len(path) - 1} steps")

if __name__ == '__main__':
    # 0 = empty space, 1 = obstacle (warehouse shelf)
    warehouse_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start_pos = (0, 0) # Charging Station
    goal_pos = (4, 4)  # Pallet Location

    print("Running Baseline A* Search...")
    optimal_path = astar(warehouse_grid, start_pos, goal_pos)

    if optimal_path:
        print(f"Path found: {optimal_path}")
        print_grid(warehouse_grid, optimal_path, start_pos, goal_pos)
    else:
        print("No valid path exists.")