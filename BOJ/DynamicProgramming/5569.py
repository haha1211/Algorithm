# 5569.출근 경로

import sys
from collections import deque

input = sys.stdin.readline
# 경로의 개수 % 100000 출력이 문제 조건
mod = 100000

m, n = map(int, input().split())

graph = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]

# 항상 오른쪽 or 아래로만 이동
# 0 -> 꺾이고 오른쪽으로 온 경우
# 다음 경로 : 꺾지 않고 오른쪽으로(2)
# 1 -> 꺾이고 아래로 온 경우
# 다음 경로 : 꺾지 않고 아래로(3) 
# 2 -> 꺾이지 않고 오른쪽으로 온 경우
# 다음 경로 : 꺾지 않고 왼쪽(2), 꺾고 아래(0)
# 3 -> 꺾이지 않고 아래로 온 경우
# 다음 경로 : 꺾지 않고 아래(3), 꺾고 오른쪽(1)


# Dynamic Programming
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

# 결과 출력
print(sum(graph[n-1][m-1]) % mod)