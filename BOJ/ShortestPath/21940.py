# 21940.가운데에서 만나요

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

distance = [[float('INF')] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, d = map(int, input().split())
    distance[u][v] = d

for i in range(1,n+1):
    distance[i][i] = 0

k = int(input())
friend = list(map(int, input().split()))

# Floyd-Warshal
for k in range(1, n+1):
# k - 거쳐가는 node
    for i in range(1, n+1):
    # i - 출발
        for j in range(1, n+1):
        # j - 도착
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

# 왕복 거리 계산
for i in range(1, n+1):
    for j in range(i+1, n+1):
        distance[i][j] = distance[i][j] + distance[j][i]
        distance[j][i] = distance[i][j]

# (준형이와 친구들 각각) - (각 도시) 별로 걸리는 왕복시간의 최댓값 구하기
country = [float('INF')]
for i in range(1, n+1):
    max_distance = -float('INF')
    for j in friend:
        max_distance = max(max_distance, distance[i][j])
    country.append(max_distance)

# 도시 별로 구한 최대 왕복 시간 중 최솟값 구하기
result = []
min_distance = min(country)
for i in range(1, n+1):
    if country[i] == min_distance:
        result.append(i)

print(*result)