# 20440.니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마 - 1

import sys
import collections

input = sys.stdin.readline

n = int(input())

mosq = collections.defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    # Coordinate Compression
    # 범위 내에 모든 좌표에 대해 값을 저장하기에는 좌표 범위가 너무 큼
    # 주요 좌표에 대해서만 결과 저장
    # 모기 들어오고 나가는 시간에 대해서만 저장
    mosq[x] += 1
    mosq[y] -= 1

coors = list(mosq.keys())
coors.sort()

result = []
total = 0
# prefix sum
for i in coors:
    total += mosq[i]
    result.append(total)

# 모기가 최대로 있을 때의 모기 마릿수
max_num = max(result)

start = result.index(max_num)
end = start
# 나가는 시간은 열린 범위 이므로
# 최대로 있는 좌표 다음 좌표가 모기가 최대로 있는 구간의 끝(열린 구간)
while end < len(result) and result[end] == max_num:
    end += 1

print(max_num)
print(coors[start], coors[end])


    
