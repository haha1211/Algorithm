# 13549.숨바꼭질3

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

# 각 위치에 방문하는 데 걸리는 최소 시간
visited = [float('INF')] * ((max(n, k) +1) * 2)

# dijkstra
queue = [(0, n)]
visited[n] = 0

while queue:
    time, pos = heapq.heappop(queue)
    if pos == k:
        print(time)
        break
    # 0 <= n, k < 100,000
    if pos-1 >= 0 and visited[pos-1] > time+1:
        visited[pos-1] = time+1
        heapq.heappush(queue, (time+1, pos-1))
    # 현재 위치가 k보다 큰 경우 +1, *2는 확인할 필요가 없다
    if pos < k:
        if visited[pos+1] > time+1:
            visited[pos+1] = time+1
            heapq.heappush(queue, (time+1, pos+1))
        if visited[pos*2] > time:
            visited[pos*2] = time
            heapq.heappush(queue, (time, pos*2))
