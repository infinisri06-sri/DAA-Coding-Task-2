dist = [
    [0, 2, 9, 10, 7],
    [1, 0, 6, 4, 3],
    [15, 7, 0, 8, 9],
    [6, 3, 12, 0, 11],
    [9, 5, 8, 6, 0]
]

cities = [0, 1, 2, 3, 4]
min_cost = float('inf')
best_path = []

def tsp(path, visited, cost):
    global min_cost, best_path
    if len(path) == len(cities):
        total_cost = cost + dist[path[-1]][path[0]]  # return to start
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path[:]
        return

    for city in cities:
        if city not in visited:
            tsp(path + [city], visited + [city], cost + dist[path[-1]][city])


tsp([0], [0], 0)
print("Shortest path:", best_path + [0])
print("Minimum cost:",min_cost)