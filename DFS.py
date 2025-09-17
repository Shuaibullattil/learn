from collections import deque
graph = {
    1: [2, 3, 5],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3, 1]
}

def DFS(graph,start,visited):
    if start in visited:
        return
    visited.add(start)
    print(start,end=" ")
    for nei in graph[start]:
            DFS(graph,nei,visited)

visited = set()
DFS(graph,1,visited)

