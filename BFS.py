from collections import deque
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}
def BFS(graph,start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node,end=" ")
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

BFS(graph,1)



