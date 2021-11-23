# 5639.이진 검색 트리

import sys
import collections

sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

input = sys.stdin.readline

preorder = collections.deque()

# 전위 순회 결과 입력 받음
while True:
    try:
        preorder.append(int(input()))
    except:
        break

length = len(preorder)
# 이진 검색 트리의 중위 순회 결과는 트리 내의 data를 정렬한 결과와 같다는 것을 이용
inorder = sorted(preorder)

# buildTree 함수 내에서 index를 찾는 시간을 줄이기 위함
pos = collections.defaultdict(int)
for i in range(length):
    pos[inorder[i]] = i

# 전위 순회 결과와 중위 순회 결과를 토대로 원래 tree를 구현
# 문제 2263과 비슷한 알고리즘
# 전위 순회 결과를 알기 때문에 left부터 할당 (후위 순회 결과를 알 경우 right부터 할당)
def buildTree(start, end):
    if start < end and 0 <= start < length and 0 <= end <= length:
        index = pos[preorder.popleft()]
        
        node = TreeNode(inorder[index])
        node.left = buildTree(start, index)
        node.right = buildTree(index+1, end)

        return node

# 후위 순회
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

tree = buildTree(0, length)
postorder(tree)

