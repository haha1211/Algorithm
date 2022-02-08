# 18222.투에-모스 문자열

import sys

input = sys.stdin.readline

n = int(input())

# recursion
# f(x) = 1-f(x-y)
# 이때 y는 x보다 작은 수 중 가장 큰 2의 제곱근
def thue_morse(n, k):
    if n == 1:
        return 0
    n -= k
    while k :
        k //= 2
        if k < n:
            break
    return 1- thue_morse(n,k)

# n보다 작은 수 중 가장 큰 2의 제곱근 찾기
for i in range(10 ** 10):
    if 2 ** i >= n:
        k = 2 ** (i-1)            
        break

print(thue_morse(n,k))