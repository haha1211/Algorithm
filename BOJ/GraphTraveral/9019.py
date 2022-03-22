# 9019.DSLR

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    # start를 end로 바꾸는 최소한의 명령어를 생성하는 프로그램
    start, end = map(int, input().split())
    visited = [False] * 10001

    # BFS
    visited[start] = True
    queue = deque()
    queue.append((start, ''))

    while queue:
        num, cmd = queue.popleft()
        # end로 바꾸는 최소한의 명령어
        if num == end:
            print(cmd)
            break
        # D 
        tmp = (num * 2) % 10000
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, cmd+'D'))

        # S
        tmp = num - 1 if num != 0 else 9999
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, cmd+'S'))

        # L
        tmp = num
        q = num // 1000
        tmp = (tmp % 1000) * 10 
        tmp += q
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, cmd+'L'))
        
        # R
        tmp = num
        r = num % 10
        tmp -= r
        tmp //= 10
        tmp += r * 1000
        if not visited[tmp]:
            visited[tmp] = True
            queue.append((tmp, cmd+'R'))
