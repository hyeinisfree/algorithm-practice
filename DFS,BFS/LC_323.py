from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:

    vertices = [[] for _ in range(n)]

    #Build a graph
    for edge in edges:
        v0, v1 = edge
        vertices[v0].append(v1)
        vertices[v1].append(v0)
    
    #Process
    visited = set()
    comp_count = 0
    
    for idx in range(n):
        if idx not in visited:
            comp_count += 1
            
            #DFS
            seen = set()
            stack = [idx]
            seen.add(idx)
            
            while stack:        
                crnt_idx = stack.pop()
                visited.add(crnt_idx)
                next_vertices = vertices[crnt_idx]
                for next_idx in next_vertices:
                    if next_idx not in seen:
                        seen.add(next_idx)
                        stack.append(next_idx)
                        
    return comp_count