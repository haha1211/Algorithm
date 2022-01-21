# 1005.ACM Craft

import sys
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    # 각 건물 건설에 걸리는 시간
    time = list(map(int, input().split()))
    # 건물 i가 다 지어진 후에 건설 할 수 있는 건물들
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    # 각 건물을 건설완료 하는데 드는 최소 시간(0으로 초기화)
    result = [0 for _ in range(n+1)]
    Q = collections.deque()

    # topological sorting(위상정렬)
    # indegree = 0인 node(건물) queue에 추가
    for i in range(1, n+1):
        if indegree[i] == 0:
            result[i] = time[i-1]
            Q.append(i)

    while Q:
        building = Q.popleft()
        for i in graph[building]:
            indegree[i] -= 1
            # 건물을 동시에 건설할 수 있기 때문에 아래와 같이 처리
            now_time = result[building] + time[i-1]
            if now_time > result[i]:
                # i건물 이전에 지어야 할 건물들이 모두 건설돼야 i 건설 가능
                result[i] = now_time
            if indegree[i] == 0:
                Q.append(i)

    # 결과 출력
    w = int(input())
    print(result[w])
