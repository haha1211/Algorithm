# 2096.내려가기

import sys

input = sys.stdin.readline

n = int(input())
# 한 줄에 3개의 숫자만 들어옴
# dp[0] -> 이전 차례까지의 각 위치에서 최소, 최댓값
# dp[1] -> dp[0]을 이용하여 현재 각 위치에서 최소, 최댓값
dp = [[[0, 0] for _ in range(3)] for _ in range(2)]

graph = list(map(int, input().split()))

# Dynamic Programming
# 가장 처음은 처음 입력받은 값으로 초기화
for i in range(3):
        dp[0][i][0] = dp[0][i][1] = graph[i]

for i in range(n-1):
    graph = list(map(int, input().split()))

    # 0번 -> 0, 1번 확인
    dp[1][0][0] = min(dp[0][0][0], dp[0][1][0]) + graph[0]
    dp[1][0][1] = max(dp[0][0][1], dp[0][1][1]) + graph[0]

    # 1번 -> 0, 1, 2번 확인
    dp[1][1][0] = min(dp[0][0][0], dp[0][1][0], dp[0][2][0]) + graph[1]
    dp[1][1][1] = max(dp[0][0][1], dp[0][1][1], dp[0][2][1]) + graph[1]

    # 2번 -> 1, 2번 확인
    dp[1][2][0] = min(dp[0][1][0], dp[0][2][0]) + graph[2]
    dp[1][2][1] = max(dp[0][1][1], dp[0][2][1]) + graph[2]

    # dp[1]을 dp[0] 위치로 바꾼 후 dp[1] 초기화
    dp[0] = dp[1]    
    dp[1] = [[0, 0] for _ in range(3)]

# 결과 출력
print(max(map(max, dp[0])), min(map(min, dp[0])))

        