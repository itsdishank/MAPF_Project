import time
from baseline_astar import astar

def run_scaling_test():
    print("--- Experiment 1: Scaling Baseline A* ---")
    
    # 5x5 Grid
    grid_5 = [[0]*5 for _ in range(5)]
    grid_5[2][1:4] = [1, 1, 1] # Small wall
    start_time = time.time()
    path_5 = astar(grid_5, (0,0), (4,4))
    print(f"5x5 Grid: Path Length = {len(path_5)-1}, Time = {(time.time() - start_time):.5f} seconds")

    # 10x10 Grid (Empty)
    grid_10 = [[0]*10 for _ in range(10)]
    start_time = time.time()
    path_10 = astar(grid_10, (0,0), (9,9))
    print(f"10x10 Grid: Path Length = {len(path_10)-1}, Time = {(time.time() - start_time):.5f} seconds")

    # 20x20 Grid (Empty)
    grid_20 = [[0]*20 for _ in range(20)]
    start_time = time.time()
    path_20 = astar(grid_20, (0,0), (19,19))
    print(f"20x20 Grid: Path Length = {len(path_20)-1}, Time = {(time.time() - start_time):.5f} seconds")

if __name__ == '__main__':
    run_scaling_test()