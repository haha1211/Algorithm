# 7453.합이 0인 네 정수

import sys

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

result = 0
subset_a = []
subset_b = []

# meet in the middle
# A,B / C,D로 나눠서 각 배열의 원소끼리 더했을 때 나올 수 있는 모든 경우 구하기
for i in range(n):
    for j in range(n):
        subset_a.append(A[i]+B[j])
        subset_b.append(C[i]+D[j])

# two pointer를 위한 정렬
subset_a.sort()
subset_b.sort()

# two pointer
result = 0
# left -> subset_a, right -> subset_b 탐색
left, right = 0, len(subset_b)-1
while left < len(subset_a) and right >=0:
    total = subset_a[left] + subset_b[right]
    if total == 0:
        # 각 배열에 같은 수가 여러개 들어갈 수 있으므로 그 경우를 확인하고 결과에 반영하는 logic
        next_left, next_right = left+1, right-1
        while next_left < len(subset_a) and subset_a[next_left] == subset_a[left]:
            next_left += 1
        while next_right >= 0 and subset_b[right] == subset_b[next_right]:
            next_right -= 1
        result += (next_left - left) * (right - next_right)
        left, right = next_left, next_right
    # 
    elif total > 0 :
        right -= 1
    else:
        left += 1

# 결과 출력
print(result)

# 참고 : https://velog.io/@ckstn0778/백준-7453번-합이-0인-네-정수-X-1
    