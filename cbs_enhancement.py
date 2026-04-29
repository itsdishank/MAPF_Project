import heapq
import copy
from baseline_astar import astar

class HighLevelNode:
    def __init__(self):
        self.constraints = [] # List of tuples: (agent_id, location, timestep)
        self.solution = {}    # Dictionary: {agent_id: path}
        self.cost = 0         # Sum of Costs (SOC)
        self.h = 0            # NEW: h-CBS Heuristic (estimated remaining conflicts)
        
    def __lt__(self, other):
        # Primary priority: Lowest Sum of Costs
        if self.cost == other.cost:
            # Secondary priority (h-CBS): Tie-break by picking the node with fewer conflicts
            return self.h < other.h
        return self.cost < other.cost

def get_location(path, time):
    """Helper to return an agent's location at a specific time. Agents wait at goal when finished."""
    if time < len(path):
        return path[time]
    else:
        return path[-1]

class CBS_MAPF_Solver:
    def __init__(self, grid, agents):
        self.grid = grid
        self.agents = agents # Format: {'agent1': {'start': (x,y), 'goal': (x,y)}, ...}
        self.open_list = []
        
    def find_first_conflict(self, solution):
        agent_ids = list(solution.keys())
        for i in range(len(agent_ids)):
            for j in range(i + 1, len(agent_ids)):
                a1 = agent_ids[i]
                a2 = agent_ids[j]
                path1 = solution[a1]
                path2 = solution[a2]
                
                max_time = max(len(path1), len(path2))
                
                for t in range(max_time):
                    loc1_t = get_location(path1, t)
                    loc2_t = get_location(path2, t)
                    
                    # Detect Vertex Conflict
                    if loc1_t == loc2_t:
                        return {'type': 'vertex', 'time': t, 'location': loc1_t, 'agents': [a1, a2]}
                    
                    # Detect Edge Conflict
                    if t > 0:
                        loc1_prev = get_location(path1, t - 1)
                        loc2_prev = get_location(path2, t - 1)
                        if loc1_t == loc2_prev and loc1_prev == loc2_t:
                            # FIX: Constrain them from entering their intended targets at time t
                            return {'type': 'edge', 'time': t, 'location': (loc1_t, loc2_t), 'agents': [a1, a2]}
        return None
        
    def count_all_conflicts(self, solution):
        """h-CBS Heuristic: Scans the entire solution and returns the total number of conflicts."""
        conflict_count = 0
        agent_ids = list(solution.keys())
        for i in range(len(agent_ids)):
            for j in range(i + 1, len(agent_ids)):
                a1 = agent_ids[i]
                a2 = agent_ids[j]
                path1 = solution[a1]
                path2 = solution[a2]
                
                max_time = max(len(path1), len(path2))
                for t in range(max_time):
                    loc1_t = get_location(path1, t)
                    loc2_t = get_location(path2, t)
                    
                    if loc1_t == loc2_t:
                        conflict_count += 1
                    elif t > 0:
                        loc1_prev = get_location(path1, t - 1)
                        loc2_prev = get_location(path2, t - 1)
                        if loc1_t == loc2_prev and loc1_prev == loc2_t:
                            conflict_count += 1
                            
        return conflict_count
    
    def solve(self):
        root = HighLevelNode()
        closed_set = set() # NEW: Enhancement 3 - State Hashing
        
        # 1. Generate root node with independent A* paths
        for agent_id, data in self.agents.items():
            path = astar(self.grid, data['start'], data['goal'])
            if not path:
                return None # Unsolvable even independently
            root.solution[agent_id] = path
            root.cost += len(path) - 1
            
        root.h = self.count_all_conflicts(root.solution)
        heapq.heappush(self.open_list, root)
        
        while self.open_list:
            current_node = heapq.heappop(self.open_list)
            
            # NEW: Enhancement 3 - Prune duplicate constraint states
            # We use frozenset because standard lists cannot be hashed into a set
            constraint_hash = frozenset(current_node.constraints)
            if constraint_hash in closed_set:
                continue # Skip this node, we have already evaluated this exact reality!
            closed_set.add(constraint_hash)
            
            conflict = self.find_first_conflict(current_node.solution)
            
            # If no conflicts exist, we found the optimal collision-free path!
            if not conflict:
                return current_node.solution
                
            # Branch realities to resolve the conflict
            for agent_id in conflict['agents']:
                child_node = HighLevelNode()
                child_node.constraints = copy.deepcopy(current_node.constraints)
                child_node.solution = copy.deepcopy(current_node.solution)
                
                # Create the new constraint
                if conflict['type'] == 'vertex':
                    new_constraint = (agent_id, conflict['location'], conflict['time'])
                else: 
                    # For edge conflicts, prevent the agent from entering its target node at time t
                    idx = conflict['agents'].index(agent_id)
                    loc_target = conflict['location'][idx] 
                    new_constraint = (agent_id, loc_target, conflict['time'])
                    
                child_node.constraints.append(new_constraint)
                
                # Re-run A* for this specific agent with its newly updated constraints
                agent_constraints = [(c[1], c[2]) for c in child_node.constraints if c[0] == agent_id]
                new_path = astar(self.grid, self.agents[agent_id]['start'], self.agents[agent_id]['goal'], agent_constraints)
                
                if new_path:
                    child_node.solution[agent_id] = new_path
                    child_node.cost = sum(len(p) - 1 for p in child_node.solution.values())
                    child_node.h = self.count_all_conflicts(child_node.solution) 
                    heapq.heappush(self.open_list, child_node)
                    
        return None

if __name__ == '__main__':
    # A brutal test: Two agents crossing a narrow 5x5 hallway in opposite directions
    test_grid = [[0]*5 for _ in range(5)]
    test_agents = {
        'agent1': {'start': (2, 0), 'goal': (2, 4)},
        'agent2': {'start': (2, 4), 'goal': (2, 0)}
    }
    
    print("Testing CBS Multi-Agent Planner...")
    solver = CBS_MAPF_Solver(test_grid, test_agents)
    solution = solver.solve()
    
    if solution:
        print("Success! Collision-free paths found:")
        for a_id, path in solution.items():
            print(f"{a_id}: {path}")
    else:
        print("Failed to find a solution.")