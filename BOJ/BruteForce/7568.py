# 7568.덩치

import sys

input = sys.stdin.readline

n = int(input())
body = []
# 몸무게 정보, 번호 저장
for i in range(n):
    x, y = map(int, input().split())
    body.append((x,y,i))


rank = [0] * n

for i in range(n):
    large = 1
    # 각 사람 별로 그 사람보다 덩치가 큰 사람들 찾기
    # 등수는 자신보다 덩치큰 사람 +1이므로 1부터 시작
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            large += 1
    # 처음 저장했던 번호에 맞춰서 등수 저장
    rank[body[i][2]] = large

print(*rank)
