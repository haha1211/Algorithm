import sys

input = sys.stdin.readline

def check_ap(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
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
    check_ap(157)
    for i in range(100, n+1):
        if check_ap(i):
            total += 1

        
print(total)