# 2110.공유기 설치

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
home = []

# 집의 위치
for _ in range(n):
    home.append(int(input()))
home.sort()

left, right = 1, home[-1]
result = 0

while left <= right:
    # 중간값 = 공유기 사이의 간격
    mid = left + (right-left) // 2
    # total = 설치 가능한 공유기 수
    total = 1
    wifi = home[0]
    for i in home:
        if i - wifi >= mid:
            total += 1
            wifi = i
    if total < c:
        right = mid -1
    # 설치하는 공유기 수가 c보다 많아져도 괜찮다
    # 설치 가능한 공유기 중 거리가 최대인 2개의 인접한 공유기 수만큼 c개 고르면 되기 때문
    else:
        left = mid +1
        result = mid

print(result)
