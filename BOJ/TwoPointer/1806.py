# 1806.부분합

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

# result를 나올 수 있는 최댓값 +1로 설정
result = n+1
left, right = 0, 0
# sum = sequence[left]부터 sequence[right]까지의 부분합
# 처음은 left=right=0이므로 sequence[left]로 설정
sum = sequence[left]

while left <= right and right <= n-1:
    # 부분합이 s보다 큰 경우의 가장 짧은 길이를 구해야 함
    if sum >= s:
        result = min(result, right-left +1)
        # 범위를 줄여주는 것이므로 원래 왼쪽 끝 값을 빼준 다음에 left 조정
        sum -= sequence[left]
        left += 1
    else:
        # sequence의 index 넘어가는 경우
        if right == n-1:
            break
        # 범위를 늘린다음에(right 조정한 다음에) 오른족 끝 값을 더해줘야함
        right += 1
        sum += sequence[right]

# 처음 초기값과 같을 경우 부분합이 s이상인 경우가 없음
if result == n+1:
    print(0)
else:
    print(result)