# 1446.지름길
# 참고 : https://konghana01.tistory.com/329

import sys

input = sys.stdin.readline

n, d = map(int, input().split())

path = []
for _ in range(n):
    x, y, length = map(int, input().split())
    # 지름길 사용이 불가한 경우(고속도로 역주행X) 제외
    if y > d:
        continue
    # 지름길이 더 오래 걸리는 경우 제외
    if y-x <= length:
        continue
    path.append([x,y,length])
# 내림차순 정렬
path.sort(reverse = True)

# Dynamic Programming
dp = [100001] * (d+1)
dp[0] = 0

for i in range(d):
    # 같은 시작점의 지름길이 여러개 있을 수 있음
    while path and i == path[-1][0]:
        x, y, length = path.pop()
        # 지름길로 가는 경우 y까지 가는 데 운전하는 거리 저장
        dp[y] = min(dp[y], dp[x] + length)
    else:
        # 0번부터 시작하는 지름길이 있을 수도 있음
        dp[i+1] = min(dp[i]+1, dp[i+1])

print(dp[d])
