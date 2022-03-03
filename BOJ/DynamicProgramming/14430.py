# 14430.자원 캐기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 자원 정보
graph = []
dp = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    dp.append([0] * m)

# Dynamic Programming
dp[0][0] = graph[0][0]

for i in range(n):
    for j in range(m):
        # 오른쪽 확인
        if j+1 < m :
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + graph[i][j+1])
        # 아래 확인
        if i+1 < n :
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+graph[i+1][j])

# 탐색할 수 있는 자원의 최대 숫자
print(dp[n-1][m-1])