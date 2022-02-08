# 4673.셀프 넘버
# 셀프 넘버 : 생성자가 없는 숫자

import numbers

nums = [False] * (10001)

def sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10

    return total


for i in range(10000):
    # i의 분해합 num을 구한 후 num을 True로
    # 생성자가 존재함을 표시
    num = i + sum(i)
    # 범위 내에서만 위 과정 진행
    if num <= 10000:
        nums[num] = True

# 생성자가 없는 셀프 넘버들 출력
for i in range(10001):
    if nums[i] == False:
        print(i)
