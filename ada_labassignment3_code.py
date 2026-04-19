from collections import deque
import heapq

print("===== GRAPH REPRESENTATION =====")

# Adjacency List
graph_list = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}

# Adjacency Matrix
graph_matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print("Adjacency List:", graph_list)
print("Adjacency Matrix:")
for row in graph_matrix:
    print(row)


print("\n===== BFS (Breadth First Search) =====")

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

bfs(graph_list, 0)


print("\n\n===== DFS (Depth First Search) =====")

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

dfs(graph_list, 0)


print("\n\n===== Topological Sort =====")

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}

    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    print("Topological Order:", topo_order)

topological_sort(graph_list)


print("\n===== Dijkstra Algorithm =====")

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print("Shortest Distances:", distances)

# Weighted Graph
graph_weighted = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

dijkstra(graph_weighted, 0)


print("\n===== Bellman-Ford Algorithm =====")

def bellman_ford(edges, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    print("Distances:", dist)

edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]

bellman_ford(edges, 4, 0)


print("\n===== Prim’s Algorithm (MST) =====")

def prim(graph):
    start = 0
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)

    mst_cost = 0

    while edges:
        weight, frm, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            mst_cost += weight

            for next_node, next_weight in graph[to]:
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, to, next_node))

    print("MST Cost:", mst_cost)

graph_mst = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

prim(graph_mst)


print("\n===== END OF ASSIGNMENT =====")