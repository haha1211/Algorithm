import sys
from collections import deque

input = sys.stdin.readline
mod = 100000

m, n = map(int, input().split())

graph = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]

# 0 -> 꺾이고 왼쪽에서 온 경우
# 1 -> 꺾이고 위에서 온 경우
# 2 -> 꺾이지 않고 왼쪽에서 온 경우
# 3 -> 꺾이지 않고 오른쪽에서 온 경우

graph[0][0][0] = 1
graph[0][0][1] = 1
for i in range(n):
    for j in range(m):
        if j + 1 < m:
            graph[i][j+1][2] += graph[i][j][0]
            graph[i][j+1][2] += graph[i][j][2]
            graph[i][j+1][0] += graph[i][j][3]
        if i + 1 < n:
            graph[i+1][j][3] += graph[i][j][1]
            graph[i+1][j][1] += graph[i][j][2]
            graph[i+1][j][3] += graph[i][j][3]

print(sum(graph[n-1][m-1]) % mod)