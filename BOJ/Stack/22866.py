import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
buildings = list(map(int, input().split()))

result = [[0,10**9] for _ in range(n)]

stack = [[0]]

for i in range(1, n):
    a = [i]
    while stack and buildings[stack[-1][0]] < buildings[i]:
        nodes = stack.pop()
        for node in nodes:
            result[node][0] += 1
            if abs((node+1)-result[node][1]) > abs((node+1)-(i+1)):
                result[node][1] = i+1
        a += nodes

    if stack and buildings[stack[-1][0]] >= buildings[i]:
        tmp = stack[-1][0]
        if buildings[tmp] == buildings[i]:
            result[i][0] = result[tmp][0]
            result[i][1] = result[tmp][1]
        else:
            result[i][0] += result[tmp][0] + 1
            if abs((i+1)-result[i][1]) > abs((i+1) - (tmp+1)):
                result[i][1] = tmp+1
            
    stack.append(a)


for i, max_num in result:
    if i == 0:
        print(0)
    else:
        print(i, max_num)
