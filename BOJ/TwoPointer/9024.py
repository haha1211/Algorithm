# 두 수의 합

import sys
import bisect

input = sys.stdin.readline

# k와 가장 가까운 합인지 확인 후 갯수 업데이트
def check_total(k, new, difference, total):
    # 기존에 합들만큼 가까운 경우
    if difference == abs(k - new):
        total += 1
    # 현재 합이 기존 것들보다 k와 더 가까운 경우
    elif difference > abs(k - new):
        difference = abs(k - new)
        total = 1
    
    return difference, total


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    # Two Pointer
    left, right = 0, n-1
    difference = 10 ** 9
    total = 0

    # 서로 다른 두 정수의 합
    while left < right:
        new = nums[left] + nums[right]
        # k와 가장 가까운 합인지 check
        difference, total = check_total(k, new, difference, total)
        if new == k:
            left += 1
            right -= 1
        elif new > k:
            right -= 1
        else:
            left += 1
    
    print(total)


    
