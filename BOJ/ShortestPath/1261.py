# 1261.알고스팟

import sys
import heapq

input = sys.stdin.readline
# 갈 수 있는 4가지 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 가로크기 = m, 세로크기 = n
m, n = map(int, input().split())

graph = []
dist = []
for _ in range(n):
    # 미로 정보
    graph.append(list(map(int, input().rstrip())))
    # 각 위치에 도착하기까지 부숴야 하는 최소 벽 수
    dist.append([float('INF')] * m)

# dijkstra
queue = [(0,0,0)]
dist[0][0] = 0

while queue:
    crush, x, y = heapq.heappop(queue)
    # (n, m) 도착
    if x == n-1 and y == m-1:
        print(crush)
        break
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m:
            # 벽인 경우 1 => 부숴야 하는 경우의 수 +1
            alt = crush + graph[xx][yy]
            # 가보지 않은 방의 경우에만 queue에 추가
            if dist[xx][yy] > alt:
                dist[xx][yy] = alt
                heapq.heappush(queue, (alt, xx, yy))

