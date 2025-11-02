class Graph:
    def __init__(self, edges):
        self.edges = edges

    def h(self, node):
        h_cost = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        return h_cost[node]

    def a_star(self, start, goal):
        to_visit = [start]
        visited = []
        cost = {start: 0}
        parent = {start: None}

        while to_visit:
            current = min(to_visit, key=lambda x: cost[x] + self.h(x))

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                print("Path found:", path[::-1])
                return

            to_visit.remove(current)
            visited.append(current)

            for (neighbor, weight) in self.edges.get(current, []):
                if neighbor in visited:
                    continue
                new_cost = cost[current] + weight

                if neighbor not in to_visit or new_cost < cost.get(neighbor, float('inf')):
                    cost[neighbor] = new_cost
                    parent[neighbor] = current
                    if neighbor not in to_visit:
                        to_visit.append(neighbor)

        print("Path not found!")


graph_data = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

g = Graph(graph_data)
g.a_star('A', 'D')
