# 2263.트리의 순회

import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder 내의 val 인자 위치를 찾는 시간을 줄이기 위함
pos = [0 for _ in range(n+1)]
for i in range(n):
    pos[inorder[i]] = i

# postorder의 마지막 결과는 tree의 루트 노드이며 inorder 결과를 왼쪽, 오른쪽으로 나눔
# postorder의 뒤에서 2번째 결과는 위 결과의 오른쪽 부분을 또 반으로 나눔
# 이 특성을 이용하여 재귀 반복하다 보면 원래 tree를 구할 수 있음

def buildTree(start, end):
    if start < end and 0 <= start <n and 0<= end <= n:
        index = pos[postorder.pop()]

        node = TreeNode(inorder[index])
        node.right = buildTree(index+1, end)
        node.left = buildTree(start, index)

        return node

tree = buildTree(0, n)

stack = [tree]

# 원래 구해진 tree를 이용하여 preorder 결과를 출력

while stack:
    cur = stack.pop()
    print(cur.val, end = " ")
    temp = cur.right
    if temp :
        stack.append(temp)
    temp = cur.left
    if temp:
        stack.append(temp)
