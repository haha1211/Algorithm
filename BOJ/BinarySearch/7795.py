# 7795.먹을 것인가 먹힐 것인가

from sys import stdin
from bisect import bisect_left

input = stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Binary Search를 위한 정렬
    b.sort()

    result = 0
    for i in a:
        # Binary Search
        # index = i보다 작은 원소의 갯수
        index = bisect_left(b, i)
        result += index

    print(result)

