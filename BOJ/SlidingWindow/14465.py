# 14465.소가 길을 건너간 이유 5

import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())
crosswalk = [True] * (n+1)
# 고장난 신호등 체크
for _ in range(b):
    crosswalk[int(input())] = False

result = 0
# 1~k번까지 신호등 중 고쳐야 하는 것 확인
for i in range(1, k+1):
    if crosswalk[i] == False:
        result += 1

now = result
left, right = 1, k

# Sliding Window
while right < n:
    right += 1
    if crosswalk[right] == False:
        now += 1
    if crosswalk[left] == False:
        now -= 1
    left += 1
    # 최소의 신호등만 고치기
    result = min(result, now)

print(result)
