from collections import deque

# Recursion
def recurDFS(graph, start, visited):
    visited.append(start)
    
    for v in graph[start]:
        if v not in visited:
            recurDFS(graph, v, visited)
    
    return visited

# Iteration
def iterDFS(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        v = stack.pop()
        
        if v not in visited:
            visited.append(v)
            stack.extend(graph[v])
    return visited

def BFS(graph, start, visited):
    visited.append(start)
    queue = deque([start])
    
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                
    return visited

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

print(recurDFS(graph, 1, []))
print(iterDFS(graph, 1))
print(BFS(graph, 1, []))