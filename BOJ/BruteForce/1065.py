# 1065.한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면 그 수를 한수라 한다

import sys

input = sys.stdin.readline

# 한수인지를 확인하는 함수
def check_ap(n):
    nums = []
    # 자릿수 찾기
    while n > 0:
        nums.append(n % 10)
        n //= 10
    # 100(두 자리)이하의 수는 항상 한수
    if len(nums) < 3:
        return True
    else:
        difference = nums[0]-nums[1]
        for i in range(1, len(nums)-1):
            if difference != nums[i]-nums[i+1]:
                return False
        return True

n = int(input())
if n < 100:
    total = n
else:
    total = 99
    for i in range(100, n+1):
        if check_ap(i):
            total += 1

print(total)
