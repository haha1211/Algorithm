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
start_heap.sort()

for s, t in start_heap:
    if not end_heap:
        heapq.heappush(end_heap, (t,s))
    else:
        if end_heap[0][0] <= s:
            heapq.heappop(end_heap)
        heapq.heappush(end_heap, (t, s))

print(len(end_heap))