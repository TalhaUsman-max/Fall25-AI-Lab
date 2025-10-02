def bfs_without_queue(graph, current_points):
    if not current_points:
        return

    next_points = []
    for point in current_points:
        print(point)
        for connected in graph[point]:
            next_points.append(connected)

    bfs_without_queue(graph, next_points)
    

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_without_queue(graph, ['A'])

print("__________________________________________________________________________________")


def bfs_with_queue(graph, start):
    visited = set()      
    queue = [start]       

    while queue:
        current = queue.pop(0)  
        if current not in visited:
            print(current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)  


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_with_queue(graph, 'A')
