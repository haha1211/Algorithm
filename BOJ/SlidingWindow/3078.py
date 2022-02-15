# 3078.좋은 친구

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# 좋은 친구 => 등수 차이가 k보다 작거나 같으면서 이름 길이가 같은 친구
friend = []
# 학생들의 이름 길이 저장
for _ in range(n):
    friend.append(len(input())-1)

# 확인하고 있는 영역내에서 이름의 길이가 i인 친구들은 몇명인지 확인
best = [0] * 21
result = 0

# 0~k 영영 확인
for i in range(k+1):
    best[friend[i]] += 1

left, right = 0, k
# Sliding Window
while left < right:
    # 좋은 친구 쌍 찾기
    result += best[friend[left]]-1
    # 등수 차이가 k보다 작은 경우도 확인하기 위해서
    # left는 계속 이동
    if right < n-1:
        right += 1
        best[friend[right]] += 1
    best[friend[left]] -= 1
    left += 1

# 결과 출력
print(result)