def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()  
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)  
            adjacent_nodes = graph.get(node, [])
            for node2 in adjacent_nodes:
                if node2 not in visited:
                    new_path = list(path)
                    new_path.append(node2)
                    stack.append(new_path)
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
result = dfs(graph, start, goal)
print(result)  