# 1920.수 찾기

from bisect import bisect
import sys
import bisect

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
# Binary Search를 위한 정렬
A.sort()

m = int(input())
X = list(map(int, input().split()))

for i in X:
    # Binary Search
    index = bisect.bisect_left(A, i)
    # list에 있는 경우
    if index < n and A[index] == i:
        print(1)
    # list에 없는 경우
    else:
        print(0)


