# 19238.스타트 택시

from copy import deepcopy
from sys import stdin
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

input = stdin.readline

n, m, fuel = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 시작 위치
x, y = map(int, input().split())
x -= 1
y -= 1
# 승객 위치
start = []
# 도착지
end = []

for i in range(m):
    sx, sy, ex, ey = list(map(int, input().split()))
    start.append([sx-1, sy-1])
    end.append([ex-1, ey-1])

# 현재 위치에서 가장 가까운 승객 찾기
def find_passenger(x, y, n, m, graph, passengers):
    Q = deque()
    Q.append((x, y))
    fuel = n * n * n
    candidate = []

    # 현재 위치에서 각 위치까지 소모되는 연로
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()
        # 승객에게 가는 최소 연료보다 더 많이 소모되는 곳에 위치할 경우
        if visited[x][y] > fuel:
            break
        # 현 위치에 승객이 있는 경우 확인
        if [x, y] in passengers:
            fuel = visited[x][y]
            # 승객 후보에 추가
            candidate.append((x, y))
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 0 and visited[xx][yy] == 0:
                visited[xx][yy] = visited[x][y] + 1
                Q.append((xx, yy))
    
    # 후보가 없을 경우 => 승객에게 가지 못하는 경우
    if not candidate:
        return -1, -1
    # 같은 양의 연료가 소모될 경우 행이 작은 순, 열이 작은 순으로 선택
    candidate.sort()
    index = start.index([candidate[0][0], candidate[0][1]])
    # 처음 연료 시작은 1로 해줬으므로 -1
    return index, fuel-1

# 승객의 위치에서 도착지까지 걸리는 시간
def arrive(sx, sy, ex, ey, n, m, graph):
    Q = deque()
    Q.append((sx, sy))

    # 현재 위치에서 각 위치까지 소모되는 연로
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    while Q:
        x, y = Q.popleft()
        # 도착지
        if x == ex and y == ey:
            return visited[x][y]-1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 0 and visited[xx][yy] == 0:
                visited[xx][yy] = visited[x][y] + 1
                Q.append((xx, yy))

    # 도착지까지 못 가는 경우
    return -1


for i in range(m):
    i, spend = find_passenger(x, y, n, m, graph, start)
    # 어느 승객에게도 갈 수 없는 경우
    if spend == -1:
        fuel = -1
        break
    fuel -= spend
    # 승객에게 갈 연료가 부족한 경우
    if fuel < 0:
        fuel = -1
        break
    spend = arrive(start[i][0], start[i][1], end[i][0], end[i][1], n, m, graph)
    # 도착지에 갈 수 없는 경우
    if spend == -1:
        fuel = -1
        break
    fuel -= spend
    # 도착지에 갈 연료가 부족한 경우
    if fuel < 0:
        fuel = -1
        break
    # 도착지에서 연료 충전
    fuel += spend * 2
    x, y = end[i][0], end[i][1]
    # 이미 태운 승객임을 표시
    start[i][0], start[i][1] = -1, -1

print(fuel)