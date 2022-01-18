# 2805.나무 자르기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

left, right = 1, max(tree)
result = 0

# Parametric Search

while left <= right:
    total = 0
    mid = left + (right-left) // 2
    # mid => 나무 자르는 톱의 위치(이 이상이 잘림)
    total = sum(i - mid if i > mid else 0 for i in tree)
    # 더 많이 잘라야 하므로 right 조정
    if total < m:
        right = mid -1
    # m에 최대한 가까이 자르기 위해 left 조정
    elif total > m :
        left = mid +1
        result = mid
    # m일 경우 while문 종료
    else:
        result = mid
        break

print(result)
        
