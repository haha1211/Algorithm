# 2213.트리의 독립집합

import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [[0]*2 for _ in range(n+1)]

# node의 가중치
weight = [0] + list(map(int, input().split()))

while True:
    try : 
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    except:
        break

# dfs
def dfs(cur):
    if visited[cur] :
        return

    visited[cur] = True
    dp[cur][0] = weight[cur]
    dp[cur][1] = 0

    for i in graph[cur]:
        if visited[i]: 
            continue

        dfs(i)

        # Dynamic Programming
        # 독립집합에 현재 node가 포함이 되는 경우(자식 node는 독립집합 포함X)
        dp[cur][0] += dp[i][1]
        # 독립집합에 현재 node가 포함이 되지 않는 경우(자식 node는 독립집합 포함 여부 상관X)
        dp[cur][1] += max(dp[i][0], dp[i][1])


# 독립집합에 속하는 node 찾기
def trace(cur, prev):
    # 이전 node가 독립집합에 포함되지 않으면서 dp[cur][0] > dp[cur][1]인 경우 => 독립집합O
    if dp[cur][0] > dp[cur][1] and not visited[prev]:
        path.append(cur)
        visited[cur] = True

    for i in graph[cur]:
        if i == prev:
            continue
        trace(i, cur)
    

dfs(1)

visited = [False] * (n+1)
path = []
trace(1,1)
path.sort()

print(max(dp[1][0], dp[1][1]))
print(*path)

