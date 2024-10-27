import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue to hold nodes to explore
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    came_from = {}
    
    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for neighbor, cost in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))

    return None  # If no path is found

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 4), ('D', 3)],
    'D': [('B', 2), ('C', 3), ('E', 5)],
    'E': [('D', 5)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

path = best_first_search(graph, 'A', 'E', heuristic)
print("Best First Search Path:", path)
