# 11000.강의실 배정

import sys
import heapq

input = sys.stdin.readline

n = int(input())
start_heap = []
end_heap = []

for _ in range(n):
    s, t = map(int, input().split())
    start_heap.append((s, t))
# 강의 시작 시간 오름차순 정렬
start_heap.sort()

for s, t in start_heap:
    # 현재 강의하고 있는 수업이 없는 경우
    if not end_heap:
        heapq.heappush(end_heap, (t,s))
    else:
        # 새로 시작할 강의 시작 시간 전에 끝나는 경우
        if end_heap[0][0] <= s:
            heapq.heappop(end_heap)
        heapq.heappush(end_heap, (t, s))

# 최소로 사용하는 강의실 수
print(len(end_heap))