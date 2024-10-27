def beam_search(graph, start, goal, heuristic, beam_width):
    open_set = [[start]]

    while open_set:
        # Get the current level of nodes
        current_level = open_set.pop(0)

        if current_level[-1] == goal:
            return current_level

        next_level = []

        for node in current_level:
            for neighbor, cost in graph[node]:
                if neighbor not in current_level:
                    next_level.append(neighbor)

        # Sort next level by heuristic and keep only the top 'beam_width' nodes
        next_level.sort(key=lambda x: heuristic[x])
        open_set.append(current_level + next_level[:beam_width])

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

# Example usage:
beam_path = beam_search(graph, 'A', 'E', heuristic, beam_width=2)
print("Beam Search Path:", beam_path)
