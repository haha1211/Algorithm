# 1504.특정한 최단 경로

import sys
import collections
import heapq

V, E = map(int, input().split())

graph = collections.defaultdict(list)

for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    # 방향성이 없는 그래프
    graph[u].append((v,w))
    graph[v].append((u,w))


# dijkstra
def dijkstra(src):
    Q = [(0, src)]
    dist = [float("INF") for _ in range(V+1)]

    while Q:
        time, node = heapq.heappop(Q)
        if dist[node] > time:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    return dist

# 반드시 지나가야 하는 두 정점
v1, v2 = map(int, input().split())

# 1번에서 V번으로 이동
one = dijkstra(1)
vone = dijkstra(v1)
vtwo = dijkstra(v2)

# '1번 ~ v1, v1 ~ v2, v2 ~ V' 또는 '1번 ~ v2, v2 ~ v1, v1 ~ V' 를 각각 구하기
# 구한 값으로 최단 경로의 길이 구하기
path = min(one[v1] + vone[v2] + vtwo[V], one[v2] + vtwo[v1] + vone[V])

if path < float("INF"):
    print(path)
# 2개의 정점을 지나가는 경로가 없는 경우
else:
    print(-1)



