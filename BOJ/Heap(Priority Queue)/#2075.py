# 2075.N번째 큰 수

import sys
import heapq

input = sys.stdin.readline

n = int(input())
# minheap
Q = []

# minheap에 초기값 저장(n개 만큼 => 처음 입력받는 줄)
# minheap에는 n개만 저장
a = list(map(int, input().split()))
for i in a:
    heapq.heappush(Q, i)

for _ in range(n-1):
    a = list(map(int, input().split()))
    for j in a:
        # n번째 큰 수를 구하기 위해 가장 작은 값과 새로운 값을 비교 후 pop&push
        if j > Q[0]:
            heapq.heappop(Q)
            heapq.heappush(Q, j)

# minheap에 입력 받은 숫자 중 가장 큰 n개의 수를 저장하였으므로 n번째 큰 수는 Q[0]
print(Q[0])
