# 9996.한국이 그리울 땐 서버에 접속하지

import sys

input = sys.stdin.readline

n = int(input())
# '*'을 기준으로 prefix, suffix 나누기
pattern = list(input().split('*'))

def check(pattern, string):
    # prefix check
    if string.find(pattern[0]) != 0:
        return False
    # suffix check
    if string.find(pattern[1], len(pattern[0])) != len(string)-len(pattern[1]):
        return False
    return True

for _ in range(n):
    if check(pattern, input()):
        print("DA")
    else:
        print("NE")    
