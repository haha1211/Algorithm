# 1032.명령 프롬프트

import sys

input = sys.stdin.readline

n = int(input())
strings = []

for _ in range(n):
    strings.append(input().rstrip())

# 입력받은 첫번째 문자열
# 문자열 => immutable => list로 변환
current = list(strings[0])
for string in strings:
    # 같을 경우 비교 X
    if current == string:
        continue
    # 다른 문자열들과 비교
    for j in range(len(string)):
        if current[j] != string[j]:
            current[j] = "?"

# 출력
print(''.join(current))