import time
import random
from baseline_astar import astar

def generate_grid(size, density):
    grid = [[0]*size for _ in range(size)]
    obstacles = int(size * size * density)
    count = 0
    while count < obstacles:
        r = random.randint(0, size-1)
        c = random.randint(0, size-1)
        # Don't block start or goal
        if (r, c) != (0, 0) and (r, c) != (size-1, size-1) and grid[r][c] == 0:
            grid[r][c] = 1
            count += 1
    return grid

if __name__ == '__main__':
    print("Experiment 3: Obstacle Density on 15x15 Grid")
    for density in [0.10, 0.20, 0.30]:
        grid = generate_grid(15, density)
        start_time = time.time()
        path = astar(grid, (0,0), (14,14))
        elapsed = time.time() - start_time
        length = len(path)-1 if path else "No Path Found"
        print(f"Density {int(density*100)}%: Path Length = {length}, Time = {elapsed:.5f} sec")