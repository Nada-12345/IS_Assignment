from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        adjacent_nodes = graph.get(node, [])
        for node2 in adjacent_nodes:
            if node2 not in path:
                new_path = list(path)
                new_path.append(node2)
                queue.append(new_path)
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
result = bfs(graph, start, goal)
print(result) 