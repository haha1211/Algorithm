# 1715.카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())

Q = []
for _ in range(n):
    heapq.heappush(Q, int(input()))

result = 0

# 최소힙으로 구현 => 카드의 개수가 적은 순으로 정렬하는 경우가 최소 비교 횟수
# 카드가 1개일 경우, 정렬할 필요가 없다
while len(Q) >= 2:
    a = heapq.heappop(Q)
    b = heapq.heappop(Q)
    result += a + b
    heapq.heappush(Q, a+b)

print(result)