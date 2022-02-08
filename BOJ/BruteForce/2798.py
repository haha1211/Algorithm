# 2798.블랙잭

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# Brue Force
result = 0
# 카드 합이 나올 수 있는 모든 경우의 수 찾기
# 정렬 후 뒤에서부터 합을 확인 후 주어진 숫자보다 작은 경우 break를 건 후,
# 그 값들을 list에 넣어주고 마지막에 max값 출력하면 더 빠른 시간에 해결 가능

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = cards[i]+cards[j]+cards[k]
            if total <= m:
                result = max(result, total)

print(result)
