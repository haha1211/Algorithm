# 1516.게임 개발

import sys
import collections

input = sys.stdin.readline

n = int(input())
# 건물 번호가 1부터 시작하기 때문에 0번에 임의의 숫자 0 넣어줌
# 각 건물을 건설하는데 걸리는 시간
time = [0]
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    # 각 건물의 건설 시간 + 각 건물을 짓기 위해 그 전에 지어져야할 건물 번호 입력 받음
    a = list(map(int, input().split()))
    time.append(a[0])
    # 각 건물 짓기 전에 지어져할 건물 정보들 graph와 indegree에 저장
    for j in range(1, len(a)-1):
        indegree[i] += 1
        graph[a[j]].append(i)

Q = collections.deque()
# 각 건물이 완성되기까지 걸리는 최소 시간 저장
result = [0 for _ in range(n+1)]

# indegree = 0인 건물 queue에 추가
for i in range(1, n+1):
    if indegree[i] == 0:
        Q.append(i)
        result[i] = time[i]

while Q:
    building = Q.popleft()
    for i in graph[building]:
        indegree[i] -= 1
        # 건물이 동시에 지어질 수 있음
        time_now = result[building] + time[i]
        # 이전에 지어야 하는 건물이 모두 건설 완료되어야 하므로
        # 가장 늦게 건설된 건물을 기준으로 시간을 구함
        if time_now > result[i]:
            result[i] = time_now
        if indegree[i] == 0:
            Q.append(i)

# 결과 출력
for i in range(1,n+1):
    print(result[i])

