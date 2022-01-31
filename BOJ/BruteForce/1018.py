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
    for i in range(start, start+8):
        key *= -1
        for j in range(end, end+8):
            if chess[i][j] != color[key]:
                change += 1
            key *= -1
    
    return min(change, 64-change)

change = 8 * 8

for i in range(n-8, -1, -1):
    for j in range(m-8, -1, -1):
        change = min(change, check(i, j, chess, color))

print(change)