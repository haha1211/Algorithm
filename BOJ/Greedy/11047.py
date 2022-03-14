import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins  = []
for _ in range(n):
    coins.append(int(input()))

total = 0

for i in range(n-1, -1, -1):
    total += k // coins[i]
    k %= coins[i]
    if k == 0:
        break

print(total)