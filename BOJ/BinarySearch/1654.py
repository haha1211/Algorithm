# 1654.랜선 자르기

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
cable = []
for _ in range(k):
    cable.append(int(input()))

left, right = 1, max(cable)
result = 0

# Parametirc Search

while left <= right:
    total = 0
    mid = left + (right-left) // 2
    # mid => 랜선 1개의 길이
    for i in cable:
        # total => 랜선 길이가 mid일 때 만들 수 있는 총 랜선의 개수
        total += i // mid
    if total < n:
        right = mid-1
    else:
        left = mid+1
        result = mid
print(result)
