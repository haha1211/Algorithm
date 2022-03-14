# 11399.ATM

import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))

# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하기 위해서 정렬
times.sort()

total = 0
result = 0
for time in times:
    # 한 사람이 돈 인출하는 데 걸리는 시간(기다리는 시간 포함)
    total += time
    # 총 걸리는 시간의 합
    result += total

print(result)