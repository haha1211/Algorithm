# 11724.연결 요소의 개수

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    # 무방향 그래프
    graph[u].append(v)
    graph[v].append(u)

connected_component = 0

# dfs
def dfs(start, visited): 
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if visited[i]:
                continue
            else:
                stack.append(i)
                visited[i] = True

for i in range(1, n+1):
    # connected graph의 조건
    # 연결요소에 속한 모든 정점을 연결하는 경로가 있어야 함
    # 다른 연결오소에 속한 정점과 연결하는 경로가 없어야 함
    if not visited[i]:
        dfs(i, visited)
        connected_component += 1

print(connected_component)

