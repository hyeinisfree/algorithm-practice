from typing import List
from collections import deque

def topologicalOrder(graph: List[List[int]]) -> List[int]:
    vertex_num = len(graph)
    indegs = [0] * vertex_num
    for vertex in graph:
        for to_idx in vertex:
            indegs[to_idx] += 1
            
    deg0s = deque()
    
    for idx, in_deg in enumerate(indegs):
        if in_deg == 0:
            deg0s.append(idx)
            
    topo_order = []
    
    while deg0s:
        vtx0indeg = deg0s.popleft()
        topo_order.append(vtx0indeg)
        vertex = graph[vtx0indeg]
        for to_idx in vertex:
            indegs[to_idx] -= 1
            if indegs[to_idx] == 0:
                deg0s.append(to_idx)
    
    return topo_order

graph = [[1,3],[2,5],[],[2],[1],[]]
print(topologicalOrder(graph))