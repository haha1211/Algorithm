# 1450. 냅색문제

from itertools import combinations
import sys
import collections
import bisect


input = sys.stdin.readline
n, c = map(int, input().split())

object = list(map(int, input().split()))

# 주어진 배열의 범위 내에서 각 부분 집합의 합을 subset에 추가하는 함수
def dfs(index, end, sum, subset):
    subset.append(sum)
    for i in range(index, end):
        dfs(i+1, end, sum+object[i], subset)

half = n//2
subset_a = []
subset_b = []
# meet in the middle
# 중간을 기준으로 배열을 둘로 나눠서 각각 dfs 함수 호출
dfs(0, half, 0, subset_a)
dfs(half, n, 0, subset_b)

# 2개의 subset 함수 중 하나(subset_b)만 정렬
subset_b.sort()
result = 0

# 정렬되지 않은 subset_a내의 원소들을 하나씩 돌며 가방 c에 넣을 수 있는 경우 구하기
# ex. c = 4, subset_a 원소 a라 할 때 b <= 4-a인 원소들의 갯수 subset_b에서 찾아 결과에 더해주기
for subset in subset_a:
    if subset > c:
        continue
    # subset_b는 정렬되어 있기 때문에 조건에 맞는 가장 오른쪽 원소의 index +1 찾기
    # index +1 => 조건에 맞는 원소들의 갯수
    index = bisect.bisect_right(subset_b, c-subset)
    result += index

# 결과 출력
print(result)



