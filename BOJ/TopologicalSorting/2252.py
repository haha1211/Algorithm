# 2252.줄 세우기

import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[[], 0] for _ in range(n+1)]

# graph[i][0] => i보다 뒤에 서는 학생들
# graph[i][1] => i보다 앞에 서는 학생들의 수(indegree)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b][1] += 1
    graph[a][0].append(b)

# pological Sorting(위상정렬)

Q = collections.deque()

# indegree = 0인 node Q에 추가
for i in range(1, n+1):
    if graph[i][1] == 0:
        Q.append(i)

result = []
while Q:
    node = Q.popleft()
    result.append(node)
    for j in graph[node][0]:
        # 현재 node에서 나가는 edge 제거
        graph[j][1] -= 1
        # 현재 학생(node) 뒤에 서는 학생들 확인 후 indegree=0인 학생 추가
        if graph[j][1] == 0:
            Q.append(j)

print(*result)