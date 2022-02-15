# 2559.tnduf

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# 온도 입력
temperature = list(map(int, input().split()))

# 0 ~ k-1개까지의(k개) 합 => result 초기화
result = now = sum(temperature[0:k])

# Sliding Window
left, right = 0, k

while right < n:
    now += temperature[right]
    right += 1
    now -= temperature[left]
    left += 1
    result = max(result, now)

print(result)