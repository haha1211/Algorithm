# 14889.스타트와 링크

import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
teams = [x for x in range(n)]
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 팀이 만들어질 수 있는 경우의 수
teams = list(combinations(teams, n//2))
capacity = [0 for _ in range(len(teams))]

difference = 10 ** 9

# Brute Force
for i in range(len(teams) // 2):
    # combinations를 이용해 조합을 구하면
    # 가운데를 중심으로 대응되는 경우가
    # 2개의 팀으로 만들어질 수 있는 경우
    # ex. 0 & len(teams)-1 이 2개의 팀으로 만들어질 수 있는 첫 번째 경우
    team = teams[i]
    team_a = 0
    for j in range(n//2):
        for k in range(j+1, n//2):
            team_a += graph[team[j]][team[k]] + graph[team[k]][team[j]]

    team = teams[len(teams)-1-i]
    team_b = 0
    for j in range(n//2):
        for k in range(j+1, n//2):
            team_b += graph[team[j]][team[k]] + graph[team[k]][team[j]]

    # 능력치의 차이 계산
    difference = min(difference, abs(team_a - team_b))
    

print(difference)