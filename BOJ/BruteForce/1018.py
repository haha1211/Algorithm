# 1018.체스판 다시 칠하기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
chess = []
color = {-1 : 'W', 1 : 'B'}
for _ in range(n):
    chess.append(list(input().rstrip()))

def check(start, end, chess, color):
    change= 0
    key = -1
    # 시작(0, 0)이 'W'일 경우 다시 칠해야 하는 정사각형의 최소 개수 구하기
    for i in range(start, start+8):
        key *= -1
        for j in range(end, end+8):
            if chess[i][j] != color[key]:
                change += 1
            key *= -1
    
    # 시작이 'B'일 경우는 'W'일 경우와 정반대, 즉 64(전체 개수)에서 빼주면 됨
    return min(change, 64-change)

# 체스판 크기 : 8 * 8
change = 8 * 8

# 주어진 보드에서 체스판 만들 수 있는 모든 경우 확인
for i in range(n-8, -1, -1):
    for j in range(m-8, -1, -1):
        change = min(change, check(i, j, chess, color))

print(change)
