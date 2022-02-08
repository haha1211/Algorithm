# 1753.최단경로

import sys
import collections
import heapq

V, E = map(int, input().split())
k = int(input())

graph = collections.defaultdict(list)

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

Q = [(0,k)]
# 최소경로를 저장하는 list
dist = collections.defaultdict(int)

# dijkstra
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))


for i in range(1, V+1):
    if i in dist:
        print(dist[i])
    else:
        print("INF")
