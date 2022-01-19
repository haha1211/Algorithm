# 7562.나이트의 이동

import sys
import collections

input = sys.stdin.readline

# 나이트가 이동할 수 있는 경우의 수
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

n = int(input())
for _ in range(n):
    I = int(input())
    # chess판 0으로 초기화
    chess = [[0 for _ in range(I)] for _ in range(I)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    queue = collections.deque()
    queue.append((0, start[0], start[1]))
    chess[start[0]][start[1]] = 1

    # BFS
    while queue:
        count, x, y = queue.popleft()
        # 종료 위치로 갈 경우 종료
        if x == end[0] and y == end[1]:
            print(count)
            break
        for i in range(8):
            # 현재 위치에서 갈 수 있는 곳 확인 후 queue에 append
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < I and 0 <= yy < I and chess[xx][yy] == 0:
                chess[xx][yy] = 1
                queue.append((count+1, xx, yy))

