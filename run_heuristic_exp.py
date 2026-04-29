import time
from cbs_enhancement import CBS_MAPF_Solver

def run_experiment_4():
    print("--- Experiment 4: Standard CBS vs h-CBS (Heuristic Impact) ---")
    
    # Create a 10x10 grid with a central obstacle to force agents into tight corridors
    grid = [[0]*10 for _ in range(10)]
    grid[4][4:7] = [1, 1, 1]
    grid[5][4] = 1

    # 3 Agents with intersecting trajectories
    agents = {
        'agent1': {'start': (2, 2), 'goal': (8, 8)},
        'agent2': {'start': (2, 8), 'goal': (8, 2)},
        'agent3': {'start': (5, 2), 'goal': (5, 8)}
    }

    # Test 1: Standard CBS (Heuristic OFF)
    print("\nRunning Standard CBS (Heuristic OFF)...")
    solver_std = CBS_MAPF_Solver(grid, agents, use_heuristic=False, use_hashing=True)
    start_time = time.time()
    solution_std, nodes_std = solver_std.solve()
    time_std = time.time() - start_time
    
    if solution_std:
        print(f"Standard CBS: {nodes_std} nodes expanded in {time_std:.4f} seconds.")
    else:
        print("Standard CBS: Failed to find solution.")

    # Test 2: h-CBS (Heuristic ON)
    print("\nRunning h-CBS (Heuristic ON)...")
    solver_h = CBS_MAPF_Solver(grid, agents, use_heuristic=True, use_hashing=True)
    start_time = time.time()
    solution_h, nodes_h = solver_h.solve()
    time_h = time.time() - start_time
    
    if solution_h:
        print(f"h-CBS:        {nodes_h} nodes expanded in {time_h:.4f} seconds.")
    else:
        print("h-CBS: Failed to find solution.")

    # Calculate Data for the Final Report
    if solution_std and solution_h and nodes_std > 0:
        node_reduction = ((nodes_std - nodes_h) / nodes_std) * 100
        time_reduction = ((time_std - time_h) / time_std) * 100
        print("\n--- Final Data Analysis ---")
        print(f"Node Expansion Reduced By: {node_reduction:.1f}%")
        if time_reduction > 0:
            print(f"Execution Time Reduced By: {time_reduction:.1f}%")

if __name__ == '__main__':
    run_experiment_4()