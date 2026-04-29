import time
from cbs_enhancement import CBS_MAPF_Solver

def run_experiment_5():
    """
    Experiment 5: Quantitative Evaluation of State Hashing (Transposition Tables).
    Executes multiple iterations of a complex 4-agent crossing scenario to generate 
    statistically rigorous average execution times, comparing performance with and 
    without constraint node hashing.
    """
    print("--- Experiment 5: Impact of State Hashing (Transposition Tables) ---")
    
    # A symmetrical grid that forces the tree to generate duplicate constraint realities
    grid = [[0]*6 for _ in range(6)]
    grid[2][2:4] = [1, 1]
    grid[3][2:4] = [1, 1]

    # 4 Agents crossing each other diagonally in a tight space
    agents = {
        'agent1': {'start': (0, 0), 'goal': (5, 5)},
        'agent2': {'start': (0, 5), 'goal': (5, 0)},
        'agent3': {'start': (5, 0), 'goal': (0, 5)},
        'agent4': {'start': (5, 5), 'goal': (0, 0)}
    }

    runs = 10 # Statistical Rigor: Averaging over multiple runs
    
    print(f"\nRunning {runs} iterations of CBS WITHOUT Hashing...")
    total_time_no_hash = 0
    nodes_no_hash = 0
    for _ in range(runs):
        solver_no_hash = CBS_MAPF_Solver(grid, agents, use_heuristic=True, use_hashing=False)
        start = time.time()
        solution, nodes_no_hash = solver_no_hash.solve()
        total_time_no_hash += (time.time() - start)
    avg_time_no_hash = total_time_no_hash / runs

    print(f"Running {runs} iterations of CBS WITH Hashing...")
    total_time_hash = 0
    nodes_hash = 0
    for _ in range(runs):
        solver_hash = CBS_MAPF_Solver(grid, agents, use_heuristic=True, use_hashing=True)
        start = time.time()
        solution, nodes_hash = solver_hash.solve()
        total_time_hash += (time.time() - start)
    avg_time_hash = total_time_hash / runs

    print("\n--- Final Data Analysis ---")
    print(f"Without Hashing: {nodes_no_hash} nodes | Avg Time: {avg_time_no_hash:.4f} sec")
    print(f"With Hashing:    {nodes_hash} nodes | Avg Time: {avg_time_hash:.4f} sec")
    
    if avg_time_no_hash > 0:
        speedup = ((avg_time_no_hash - avg_time_hash) / avg_time_no_hash) * 100
        print(f"Execution Speed Improved By: {speedup:.1f}%")

if __name__ == '__main__':
    run_experiment_5()