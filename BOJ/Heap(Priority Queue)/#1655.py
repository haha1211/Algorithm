# 1655.가운데를 말해요

import sys
import heapq

input = sys.stdin.readline

n = int(input())

minheap = []
maxheap = []

# 가운데 값 = minheap[0] => 초기값 minheap에 추가
minheap.append(int(input()))
print(minheap[0])

for _ in range(n-1):
    new = int(input())
    # 가운데 값 기준으로 minheap, maxheap에 추가(maxheap, 가운데값(minheap[0]), minheap 순)
    if new < minheap[0]:
        heapq.heappush(maxheap, -new)
    else:
        heapq.heappush(minheap, new)
    
    # 2개의 길이가 같은 경우 가운데 두 수 중 작은 값이 들어가야하므로 maxheap에서 pop한 값 minheap에 push
    if len(minheap) == len(maxheap):
        heapq.heappush(minheap, -heapq.heappop(maxheap))
    # minheap으로 쏠렸을 경우 minheap에서 pop한 값 maxheap에 push 
    elif len(minheap) - len(maxheap) == 3:
        heapq.heappush(maxheap, -heapq.heappop(minheap))
    
    # 가운데 값
    print(minheap[0])
