# 14430.자원 캐기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    result.append([0] * m)

result[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        if j+1 < m :
            result[i][j+1] = max(result[i][j+1], result[i][j] + graph[i][j+1])
        if i+1 < n :
            result[i+1][j] = max(result[i+1][j], result[i][j]+graph[i+1][j])

print(result[n-1][m-1])