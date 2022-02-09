# 10159.저울

import sys

input = sys.stdin.readline
n = int(input())
# 무게를 비교하지 않은 쌍은 -1
graph = [[-1] * n for _ in range(n)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    # a > b일 경우 [a][b] = 1, [b][a] = 0
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 0

# Floyd-Warshall
for i in range(n):
    for j in range(n):
        for k in range(n):
            # -1 => 측정 X, 같다는 건 i를 통해 j, k의 무게 비교 결과를 알 수 있다는 의미
            if graph[j][i] != -1 and graph[j][i] == graph[i][k]:
                graph[j][k] = graph[j][i]

for node in graph:
    # -1은 측정 불가, 자기자신([1][1])의 경우를 제외하기 위해 -1
    print(node.count(-1)-1)