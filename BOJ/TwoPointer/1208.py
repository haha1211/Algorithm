# 1208.부분 수열의 합2

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

# 모든 부분집합의 원소들의 합을 구하는 함수(dfs 이용)
def dfs(start, end, sum, subset):
    subset.append(sum)
    for i in range(start, end):
        dfs(i+1, end, sum+sequence[i], subset)

# meet in the middle
# 수열을 둘로 나눠서 2개의 수열에 대한 부분집합의 원소의 합을 따로 구함 -> O(2^(n/2))
half = n // 2
subset_a = []
subset_b = []
dfs(0, half, 0, subset_a)
dfs(half, len(sequence), 0, subset_b)

# two pointer를 위한 정렬
subset_a.sort()
subset_b.sort()
result = 0

# two pointer
left, right = 0, len(subset_b)-1
# left -> subset_a, right -> subset_b 탐색
while left < len(subset_a) and right >= 0:
    total = subset_a[left] + subset_b[right]
    if total == s:
        # 각 배열에 같은 수가 여러개 들어갈 수 있으므로 그 경우를 확인하고 결과에 반영하는 logic
        i, j = left+1, right-1
        while i < len(subset_a) and subset_a[left] == subset_a[i]:
            i += 1
        while j >= 0 and subset_b[j] == subset_b[right]:
            j -=1
        result += (i-left) * (right-j)
        left, right = i, j
    elif total > s:
        right -=1
    else:
        left +=1

# 크기가 양수인 부분수열이 조건이므로 공집합 + 공집합(=0)인 경우를 빼줘야 함
if s == 0:
    result -=1
print(result)
        