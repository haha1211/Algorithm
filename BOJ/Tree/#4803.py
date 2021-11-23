# 4803.트리

import sys
import collections

input = sys.stdin.readline

count = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    # 그래프 정보 입력 받아 저장
    graph = collections.defaultdict(list)
    for _ in range(m):
        v, w = map(int, input().split())
        graph[v].append(w)
        graph[w].append(v)

    # DFS를 이용하여 그래프 내 cycle이 존재하는지 확인하여 tree 개수 찾기
    # DFS 수행을 위해 visited False로 초기화

    visited = [False for _ in range(n+1)]
    cnt = 0

    # 모든 정점 확인을 위해 for문으로 구현
    for i in range(1, n+1):

        # 이미 tree인지 확인한 정점은 pass
        if visited[i]:
            continue
        
        # stack을 이용한 DFS 구현
        stack = [(i, 0)]
        cycle = False
        while stack:
            vertex, parent = stack.pop()
            visited[vertex] = True

            for w in graph[vertex]:
                # 양방향 그래프이므로 parent와 같은지 확인
                if w == parent:
                    continue
                if visited[w]:
                    cycle = True
                else:
                    stack.append((w, vertex))
            if cycle:
                break
        
        # cycle이 아닐 경우 => tree
        if not cycle:
            cnt += 1

    # 결과 출력
    if cnt == 0:
        print("Case {}: No trees.". format(count))
    elif cnt == 1:
        print("Case {}: There is one tree.". format(count))
    else:
        print("Case {}: A forest of {} trees.". format(count, cnt))

    count += 1
