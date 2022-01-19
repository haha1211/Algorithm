# 1766.문제집

import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
problem = [[[], 0] for _ in range(n+1)]

# problem[i][0] => i 이후에 풀어야 하는 문제들
# problem[i][1] => i 이전에 풀어야 하는 문제의 갯수(0이 될 때 i 풀기 가능)
for _ in range(m):
    a, b = map(int, input().split())
    problem[a][0].append(b)
    problem[b][1] += 1

# minheap
Q = []

# pological Sorting(위상정렬)
# problem[i][1] == 0 => indegree = 0 => i를 푸는데 제약 없음 즉, 바로 풀기 가능
# 이 경우 Q에 push
for i in range(1,n+1):
    if problem[i][1] == 0:
        heapq.heappush(Q, (i, problem[i][0]))

result = []
while Q:
    x, y = heapq.heappop(Q)
    result.append(x)
    if y:
        for j in y:
            # x node에서 나가는 edge 제거
            problem[j][1] -= 1
            # x 이후 풀기 가능한 문제들 확인 후, Q에 push
            if problem[j][1] == 0:
                heapq.heappush(Q, (j, problem[j][0]))

# 결과 출력
print(*result)
