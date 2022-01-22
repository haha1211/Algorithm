from itertools import combinations
import sys
import collections
import bisect


input = sys.stdin.readline
n, c = map(int, input().split())

object = list(map(int, input().split()))

def dfs(index, end, sum, subset):
    subset.append(sum)
    for i in range(index, end):
        dfs(i+1, end, sum+object[i], subset)

half = n//2
subset_a = []
subset_b = []
dfs(0, half, 0, subset_a)
dfs(half, n, 0, subset_b)

subset_b.sort()
result = 0

for subset in subset_a:
    if subset > c:
        continue
    index = bisect.bisect_right(subset_b, c-subset)
    result += index

print(result)



