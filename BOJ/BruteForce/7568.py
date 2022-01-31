import sys

input = sys.stdin.readline

n = int(input())
body = []
for i in range(n):
    x, y = map(int, input().split())
    body.append((x,y,i))


rank = [0] * n

for i in range(n):
    large = 1
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            large += 1
    rank[body[i][2]] = large

print(*rank)
