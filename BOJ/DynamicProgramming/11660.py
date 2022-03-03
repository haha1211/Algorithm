# 11660.구간 합 구하기 5

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = []
dp.append([0] * (n+1))
for _ in range(n):
    dp.append([0] + list(map(int, input().split())))

# Dynamic Programming
# (1,1) 부터 (i,j) 까지의 합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + dp[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    # 위에서 구한 값들을 이용하여 (x1,y1) 부터 (x2,y2) 까지의 합 구하기
    total = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(total)