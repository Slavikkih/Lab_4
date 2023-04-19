import numpy as np

def bfs(residual_graph, s, t, parent):
    # Знаходимо найкоротший шлях від вершини s до вершини t за допомогою BFS алгоритму
    visited = [False] * residual_graph.shape[0]
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for index, value in enumerate(residual_graph[u]):
            if not visited[index] and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u

    return True if visited[t] else False

def ford_fulkerson(graph, source, sink):
    # Створюємо копію графа
    residual_graph = np.array(graph)
    parent = [-1] * residual_graph.shape[0]
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        # Знаходимо мінімальний потік у шляху, знайденому BFS алгоритмом
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Оновлюємо решту графа відповідно до нового потоку
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        # Додаємо максимальний потік шляху до максимального потоку
        max_flow += path_flow

    return max_flow

# Зчитуємо граф з файлу
graph = np.loadtxt("graph4.txt", dtype=int, delimiter=" ")

# Викликаємо функцію ford_fulkerson() для знаходження максимального потоку
source = 0
sink = graph.shape[0] - 1
max_flow = ford_fulkerson(graph, source, sink)
print("Максимальний потік у графі:", max_flow)
