# 16724.피리 부는 사나이

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = []
for _ in range(n):
    graph.append(list(input().strip()))
    visited.append([-1] * m)

# BFS
# visited(flag 이용)를 확인하여 이전 bfs에서 지나간 곳을 지나갈 경우
# safezone을 추가하지 않아도 되므로 0 return
# 아닐 경우 1 return
def bfs(x, y, flag):
    visited[x][y] = flag

    queue = deque()
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        # 방향에 따른 다음 이동 위치
        direction = graph[x][y]
        if direction == "U":
            x -= 1
        elif direction == "D":
            x += 1
        elif direction == "L":
            y -= 1
        elif direction == "R":
            y += 1
        if 0 <= x < n and 0 <= y < m:
            if visited[x][y] == -1:
                visited[x][y] = flag
                queue.append([x,y])
            elif visited[x][y] == flag:
                return 1
            # 이전 BFS에서 방문한 곳(safezone이 존재하는 route)을 방문하는 경우
            else:
                return 0
        else:
            return 1
                

result = 0
for i in range(n):
    for j in range(m):
        # 모든 방문하지 않은 위치에 대해 BFS
        if visited[i][j] == -1:
            result += bfs(i, j, i*n+j)

print(result)