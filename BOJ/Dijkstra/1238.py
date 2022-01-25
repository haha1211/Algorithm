import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    back_graph[v].append((u, w))

def dijkstra(start, graph):
    dist = [float("INF")] * (n+1)
    Q = [(0, start)]

    while Q:
        time, node = heapq.heappop(Q)
        if dist[node] > time:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    return dist

result = dijkstra(x, graph)
back_result = dijkstra(x, back_graph)

result = max(result[i] + back_result[i] for i in range(1, n+1))
print(result)
