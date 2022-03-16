import sys

input = sys.stdin.readline

n = int(input())
lectures = []

for _ in range(n):
    lectures.append(list(map(int, input().split())))

lectures.sort(key = lambda x : (x[1], x[0]))

end = 0
total = 0
for lecture in lectures:
    if lecture[0] >= end:
        total += 1
        end = lecture[1]

print(total)