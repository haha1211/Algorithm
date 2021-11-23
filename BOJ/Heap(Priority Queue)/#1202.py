# 1202.보석 도둑

import sys
import heapq
from bisect import bisect_right

input = sys.stdin.readline

n, k = map(int, input().split())

# 보석 정보 저장
jewel = []
for _  in range(n):
    weight, price = map(int, input().split())
    jewel.append([weight, price])
# 보석 무게 큰 순으로 정렬(pop()을 사용하기 위함)
# 새로운 값을 계속해서 넣을 것이 아니므로 heap보다는 sort를 사용하는 것이 더 효율적
jewel.sort(key=lambda x: x[0], reverse=True)

# 가방 무게 저장
bag = []
for _ in range(k):
    bag.append(int(input()))
# 가방 무게 큰 순으로 정렬(pop()을 사용하기 위함)
bag.sort(reverse = True)

capacity = []
result = 0

while bag:
    weight = bag.pop()
    while jewel:
        # 가방에 담을 수 있는 보석들을 가격 순으로 정렬(heap 사용)
        if jewel[-1][0] <= weight:
            m, v = jewel.pop()
            heapq.heappush(capacity, -v)
        else:
            break
    # 가방에 담을 수 있는 보석 중 가장 비싼 보석 담기
    if capacity:
        result -= heapq.heappop(capacity)

print(result)