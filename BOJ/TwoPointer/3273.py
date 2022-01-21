# 3273.두 수의 합

import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
# Two Pointer 사용을 위해 정렬
sequence.sort()
x = int(input())

left, right = 0, n-1
result = 0

# Two Pointer
# a+b = x일 때 a != b이므로 left < right
while left < right:
    total = sequence[left] + sequence[right]
    if total < x:
        left += 1
    elif total > x:
        right -= 1
    else:
        # a+b = x인 두 쌍을 찾았으므로 결과에 +1
        result +=1
        left += 1
        right -= 1

print(result)

