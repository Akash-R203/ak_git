from queue import PriorityQueue
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 6)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 1,
    'G': 0
}
def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start, [start])) # (f, current_node, path)
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            print("Path:", path)
            return
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g = len(path) # assuming unit cost for each step
                h = heuristic[neighbor]
                f = g + h
                pq.put((f, neighbor, path + [neighbor]))
a_star('A', 'G')