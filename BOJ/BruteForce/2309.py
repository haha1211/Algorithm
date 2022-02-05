# 2309.일곱 난쟁이

import sys
from itertools import combinations

input = sys.stdin.readline

heights = []
for i in range(9):
    heights.append(int(input()))

# 일곱 난쟁이가 될 수 있는 모는 경우 구하기
heights = combinations(heights, 7)
for height in heights:
    # 일곱 난쟁이의 키 합이 100인 경우
    if sum(height) == 100:
        for j in sorted(height):
            print(j)
        break