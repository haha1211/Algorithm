# 1644.소수의 연속합

import sys

# 에라토스테네스의 체(소수를 찾는 방법)
def eratos(n):
    prime = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i*2, n+1, i):
                prime[j] = False

    return [i for i in range(2, n+1) if prime[i] == True]

input = sys.stdin.readline
n = int(input())

prime = eratos(n)
# n=1인 경우 소수가 존재하지X (1<=n 이므로 예외처리)
if len(prime) == 0:
    print(0)
    exit()

# two pointer(문제 1806과 비슷한 풀이)
# left, right 모두 왼쪽 끝에서 시작
left, right = 0, 0
result = 0
# sum 처음값 설정(가장 왼쪽 값 -> left, right 모두 0이므로)
sum = prime[left]

while left <= right and right < len(prime):
    if sum >= n:
        # 부분합이 n인 경우에만 result +1
        if sum == n:
            result += 1
        sum -= prime[left]
        left += 1
    # index 벗어나지 않게 break
    elif right == len(prime)-1:
        break
    else:
        right += 1
        sum += prime[right]

# 결과 출력
print(result)

