import collections
import sys

input = sys.stdin.readline

n = int(input())

tree = collections.defaultdict(list)

# 트리를 인접리스트로 구현
for _ in range(n-1):
    v, w = map(int, input().split())
    tree[v].append(w)
    tree[w].append(v)

par = collections.defaultdict(int)
stack = [1]

# DFS 돌면서 각 노드의 부모 par에 저장
while stack:
    v = stack.pop()
    for node in tree[v]:
        if node not in par:
            par[node] = v
            stack.append(node)

# 정답 출력
for i in range(2, n+1):
    print(par[i])