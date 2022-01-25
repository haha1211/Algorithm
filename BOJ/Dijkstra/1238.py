import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
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

dist = [[]]
for i in range(1, n+1):
    dist.append(dijkstra(i))

result = max(dist[i][x] + dist[x][i] for i in range(1, n+1))
print(result)
