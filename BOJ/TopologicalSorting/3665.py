# 3665.최종 순위

import sys
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    # 작년 순위
    last = list(map(int, input().split()))
    # 각 node와 연결된 node들의 list(이후 순위의 팀들의 list)
    graph = [[] for _ in range(n+1)]
    indegree = [0 for O in range(n+1)]

    a = []
    indegree[last[-1]] = n-1
    a.append(last[-1])
    for i in range(n-2,-1,-1):
        cur = last[i]
        graph[cur] = a[:]
        a.append(cur)
        indegree[cur] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # 순위가 상대적으로 변한 팀들
        # 작년에 a가 높았는지, b가 높았는지를 판단하여 graph, indegree에 추가&삭제
        if indegree[a] > indegree[b]:
            graph[a].append(b)
            graph[b].remove(a)
        else:
            graph[b].append(a)
            graph[a].remove(b)

    # topological sorting(위상정렬)
    # indegree = 0인 팀(1위 팀) Q에 추가
    Q = collections.deque()
    for i in range(1, n+1):
        indegree[i] = n-1-len(graph[i])
        if indegree[i] == 0:
            Q.append(i)

    # graph내에 cycle이 있는 경우 => 일관성 없는 잘못된 정보
    # 상대적인 등수가 바뀐 쌍의 모든 경우를 알려주기 때문에 언제나 확실한 정보를 찾을 수 있음
    if len(Q) != 1:
        print("IMPOSSIBLE")
        continue
    result = []
    impossible = False
    while Q:
        team = Q.popleft()
        result.append(team)
        for i in graph[team]:
            indegree[i] -= 1
            if indegree[i] == 0:
                Q.append(i)
            # graph내 cycle이 생기는 경우
            elif indegree[i] < 0:
                impossible = True
    if not impossible and len(result) == n:
        print(*result)
    else:
        print("IMPOSSIBLE")

    
    

    

