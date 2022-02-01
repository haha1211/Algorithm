import numbers


nums = [False] * (10001)

def sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10

    return total


for i in range(10000):
    num = i + sum(i)
    if num <= 10000:
        nums[num] = True

for i in range(10001):
    if nums[i] == False:
        print(i)
