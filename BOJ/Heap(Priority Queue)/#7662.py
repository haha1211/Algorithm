# 7662.이중 우선순위 큐

import sys
import heapq

input = sys.stdin.readline

T = int(input())

# min-max heap 이용하여 풀이 => min level, max level이 번갈아가며 존재
# 참고 : https://en.wikipedia.org/wiki/Min-max_heap

def level(i):
    count = 0
    while i:
        i //= 2
        count += 1
    # max_level => True
    # min_level => False
    return count %2 == 0

# 가장 작은 값 return (root가 항상 minimum)
def minimum(heap):
    return heap[1]

# 가장 큰 값 return (첫번째 max level의 2개 원소 중 큰 값이 항상 maximum)
def maximum(heap):
    length = len(heap)
    if length == 2:
        return heap[1]
    elif length == 3:
        return heap[2]
    else:
        return max(heap[2], heap[3])

# min level에서 원소 위치 찾기(heapify)
def push_down_min(heap, i):
    length = len(heap)
    if i*2 < length:
        m = i*2
        child = True
        if i*2 + 1 < length:
            if heap[i*2] > heap[i*2 +1]:
                m = i*2 +1
            if i * 4 < length:
                for j in range(i*4, min(i*4+4, length)):
                    if heap[j] < heap[m]:
                        m = j
                        child = False
        if not child:
            if heap[m] < heap[i]:
                heap[m], heap[i] = heap[i], heap[m]
                if m//2 > 0 and heap[m] > heap[m//2]:
                    heap[m], heap[m//2] = heap[m//2], heap[m]
                push_down_min(heap, m)
        elif heap[m] < heap[i]:
            heap[m], heap[i] = heap[i], heap[m]

# max level에서 원소 위치 찾기(heapify)
def push_down_max(heap, i):
    length = len(heap)
    if i*2 < length:
        m = i*2
        child = True
        if i*2 + 1 < length:
            if heap[i*2] < heap[i*2 +1]:
                m = i*2 +1
            if i * 4 < length:
                for j in range(i*4, min(i*4+4, length)):
                    if heap[j] > heap[m]:
                        m = j
                        child = False
        if not child:
            if heap[m] > heap[i]:
                heap[m], heap[i] = heap[i], heap[m]
                if m//2 > 0 and heap[m] < heap[m//2]:
                    heap[m], heap[m//2] = heap[m//2], heap[m]
                push_down_max(heap, m)
        elif heap[m] > heap[i]:
            heap[m], heap[i] = heap[i], heap[m]

def push_down(heap, i):
    if level(i):
        push_down_max(heap, i)
    else:
        push_down_min(heap, i)

# 새로운 원소 추가되었을 때 min level에서 위치 찾기
def push_up_min(heap, i):
    if i // 4 > 0 and heap[i] < heap[i//4]:
        heap[i], heap[i//4] = heap[i//4], heap[i]
        push_up_min(heap, i//4)

# 새로운 원소 추가되었을 때 max level에서 위치 찾기
def push_up_max(heap, i):
    if i // 4 > 0 and heap[i] > heap[i//4]:
        heap[i], heap[i//4] = heap[i//4], heap[i]
        push_up_max(heap, i//4)

    # max_level => True
    # min_level => False
def push_up(heap, i):
    if i > 1:
        if level(i):
            if heap[i] < heap[i//2]:
                heap[i], heap[i//2] = heap[i//2], heap[i]
                push_up_min(heap, i//2)
            else:
                push_up_max(heap, i)
        else:
            if heap[i] > heap[i//2]:
                heap[i], heap[i//2] = heap[i//2], heap[i]
                push_up_max(heap, i//2)
            else:
                push_up_min(heap, i)

# 삽입
def insert(heap, k):
    heap.append(k)
    push_up(heap, len(heap)-1)

# 가장 작은 값 삭제
def remove_min(heap):
    if len(heap) == 2:
        heap.pop()
    else:
        heap[1] = heap.pop()
        push_down(heap, 1)

# 가장 큰 값 삭제
def remove_max(heap):
    length = len(heap)
    if length == 2 or length == 3:
        heap.pop()
    else:
        if heap[2] > heap[3]:
            i = 2 
        else:
             i = 3
        if i == length-1:
            heap.pop()
            return
        else:
            heap[i] = heap.pop()
            push_down(heap, i)


for _ in range(T):
    n = int(input())
    # root를 리스트 내 1번 index에 저장하기 위함
    Q = [0]
    for _ in range(n):
        cmd, k = input().rsplit()
        if cmd == "I":
            insert(Q, int(k))
        elif cmd == "D":
            if len(Q) > 1:
                if k == "-1":
                    remove_min(Q)
                else:
                    remove_max(Q)
    
    if len(Q) > 1:
        print(maximum(Q), minimum(Q))
    else:
        print("EMPTY")