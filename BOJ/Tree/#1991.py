# 1991.트리 순회

import sys
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

input = sys.stdin.readline

n = int(input())
tree = collections.defaultdict(list)

# tree 정보 입력 받아 저장
for _ in range(n):
    val, left, right = input().split()
    tree[val].append(left)
    tree[val].append(right)

# 입력 받은 정보를 토대로 tree 구현
def buildTree(val):
    if val == ".":
        return
    node = TreeNode(val)
    node.left = buildTree(tree[val][0])
    node.right = buildTree(tree[val][1])

    return node

# 전위 순회
def preorder(node):
    if node is None:
        return
    print(node.val, end="")
    preorder(node.left)
    preorder(node.right)

# 중위 순회
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val, end="")
    inorder(node.right)

# 후위 순회
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end="")

result = buildTree("A")

preorder(result)
print()
inorder(result)
print()
postorder(result)
print()
