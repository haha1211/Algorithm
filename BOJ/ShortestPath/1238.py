# 1238.파티

import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    # u -> v
    graph[u].append((v, w))
    # v -> u
    # 단방향 도로지만, 모든 학생들의 집에서 x로 가는 최소시간을 한 번에 구하기 위해 반대 방향에 대한 정보도 저장
    back_graph[v].append((u, w))

# dijkstra
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

# x -> 각 학생들의 마을 로 가는데 걸리는 최소시간
result = dijkstra(x, graph)
# 각 학생들의 마 -> x 로 가는데 걸리는 최소시간
back_result = dijkstra(x, back_graph)

# x로 오고 가는데 가장 오래 걸리는 학생 구하기
result = max(result[i] + back_result[i] for i in range(1, n+1))
print(result)
