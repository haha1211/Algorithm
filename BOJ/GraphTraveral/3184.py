# 3184.양

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
def bfs(x, y, graph):
    sheep = 0
    wolf = 0
    Q = deque()
    Q.append((x,y))
    graph[x][y] = '#'
    sheep += 1
    while Q:
        x, y = Q.popleft()
        # 갈 수 있는 4가지 방향
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] != '#':
                # 현재 위치에 양이 있는 경우
                if graph[xx][yy] == 'o':
                    sheep += 1
                # 현재 위치에 늑대가 있는 경우
                elif graph[xx][yy] == 'v':
                    wolf += 1
                # 현재 위치를 확인했음을 의미
                graph[xx][yy] = '#'
                Q.append((xx, yy))
    # 같은 영역 내에 존재하는 양, 늑대의 수
    return sheep, wolf

n, m = map(int, input().split())
graph = []
sheeps = []

sheep = 0
wolf = 0 

for i in range(n):
    a = list(input().rstrip("\n"))
    graph.append(a)
    for j in range(m):
        if a[j] == 'o' :
            sheeps.append((i,j))
            sheep += 1
        elif a[j] == 'v':
            wolf += 1

for (x, y) in sheeps:
    # '#'인 경우 -> 같은 영역에 있는 다른 양의 위치에서 BFS로 확인
    if graph[x][y] == 'o':
        s, w = bfs(x, y, graph)
        # 양이 늑대를 쫓아낸 경우
        if s > w:
            wolf -= w
        # 늑대가 양을 잡아먹은 경우
        else:
            sheep -= s

print(sheep, wolf)
