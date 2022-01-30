# 14502.연구소

import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []

for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

virus_list = []
wall = []
wall_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i*m)+j)
        elif graph[i][j] == 2:
            virus_list.append((i, j))
        else:
            wall_num += 1
wall = list(combinations(wall,3))


def bfs(graph, wall, virus_list,n, m, wall_num):
    for i in wall:
        graph[i//m][i%m] = 1
        wall_num += 1

    queue = deque()
    for x, y in virus_list:
        queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        wall_num += 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 0:
                graph[xx][yy] = 2
                queue.append((xx, yy))
    return n *m - wall_num

safety = 0
for i in wall:
    count = bfs(deepcopy(graph), i, virus_list, n, m, wall_num)
    safety = max(safety, count)

print(safety)
