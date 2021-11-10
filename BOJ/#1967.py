# 1967.트리의 지름 (#1167과 입력 방식만 다름)

import sys
import collections

input = sys.stdin.readline

n = int(input())
tree = collections.defaultdict(list)

# tree 정보 인접리스트로 저장
for _ in range(n-1):
    v, w, cost = map(int, input().split())
    tree[v].append((w,cost))
    tree[w].append((v, cost))

# start에서 가장 먼 점 & 거리 구하는 함수

def DFS(start):
    length = 0
    vertex = start
    visit = [False] * (n+1)
    visit[start] = True
    stack = [(start,0)]

    while stack:
        v, total = stack.pop()
        for w, cost in tree[v]:
            if visit[w] == False:
                visit[w] = True
                if length < total+cost:
                    length = total+cost
                    vertex = w
                stack.append((w, cost+total))
        
    return vertex, length

# 트리의 지름 구하는 알고리즘
# 1. 아무 점에서 가장 먼 점 t 구하기
# 2. t에서 가장 먼 점 u 구하기
# 3. t-u 가 트리의 지름


v1, leng = DFS(1)
v2, leng = DFS(v1)

print(leng)