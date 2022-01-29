# 7576.토마토

import sys
import collections

# 하나의 토마토와 인접한 네 방향들
dx = [-1,1,0,0]
dy = [0,0,1,-1]

input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
queue = collections.deque()
have = 0
for i in range(n):
    graph.append(list(map(int, input().rstrip().split(" "))))
    for j in range(m):
        # 익은 토마토
        if graph[i][j] == 1:
            queue.append((i,j))
        # 익지 않은 토마토
        elif graph[i][j] == 0:
            have += 1

days = 1
# BFS
while queue:
    x, y = queue.popleft()
    day = graph[x][y]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy <m and graph[xx][yy] == 0:
            # 토마토가 모두 익을 때가지의 날짜
            if days < day + 1:
                days = day + 1
            # 토마토가 인접한 토마토의 영향으로 익은 경우
            graph[xx][yy] = day + 1
            have -= 1
            queue.append((xx, yy))

# 익지 않은 토마토들이 존재하는 경우
if have:
    print(-1)
else:
    print(days - 1)