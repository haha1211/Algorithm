# 15961.회전 초밥

import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

dish = []
sushi = [0] * (d+1)
for _ in range(n):
    dish.append(int(input()))
# 회전 초밥이기에 k-1만큼 뒤에 추가(k개씩만 선택)
for i in range(k-1):
    dish.append(dish[i])

result = 0
# 쿠폰으로 제공되는 초밥
sushi[c] += 1
num = 1

left = right = 0

# 슬라이딩 윈도우
while right < len(dish):
    # 오른쪽에 하나 추가할 때 가짓수 체크
    if sushi[dish[right]] == 0:
        num += 1
    sushi[dish[right]] += 1
    right += 1
    # k개가 안되는 경우 left 옮기지 않음
    if right <= k:
        # k개일 때 가짓수 저장
        if right == k:
            result = max(result, num)
        continue
    # 왼쪽에서 하나 뺄 때 가짓수 체크
    sushi[dish[left]] -= 1
    if sushi[dish[left]] == 0:
        num -= 1
    left += 1
    # 최대 가짓수 비교 후 저장
    result = max(result, num)

print(result)
