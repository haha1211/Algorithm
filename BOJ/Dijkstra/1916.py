# 1916. 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [float("INF")] * (n+1)
# 버스 정보 저장
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

# 출발, 도착 도시 번호
start, end = map(int, input().split())

# dijkstra
Q = [(0, start)]
while Q:
    time, node = heapq.heappop(Q)
    if node == end:
        print(time)
        break
    if dist[node] > time:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))