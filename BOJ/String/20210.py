# 20210.파일 탐색기

import sys
import re

input = sys.stdin.readline

n = int(input())
strings = []

for _ in range(n):
    string = input().strip()
    # 연속되는 숫자 부분 하나의 원소로 나누기
    # 문자 각각은 그대로 하나하나가 원소
    tmp = re.findall("[a-zA-Z]|\d+", string)
    strings.append(tmp)

# 문제에서 주어진 natural sort
# a->b 일 때 True
# b->a 일 때 False
def natural_sort(a, b):
    i = j = 0
    while i < len(a) and j < len(b):
        # 둘 다 숫자일 경우
        if a[i].isdigit() and b[j].isdigit():
            zero_a = a[i].count('0')
            num_a = int(a[i])

            zero_b = b[j].count('0')
            num_b = int(b[j])

            # 숫자가 같은 경우
            if num_a == num_b:
                # 숫자, 0의 갯수 모두 똑같은 경우 다음 순서로 넘어감
                if zero_a == zero_b:
                    i += 1
                    j += 1
                else:
                    # 다를 경우 0의 갯수가 적은 경우가 앞
                    return zero_a < zero_b
            else:
                # 숫자가 다른 경우 작은 숫자가 앞
                return num_a < num_b
        # 두 문자가 같은 경우
        elif a[i] == b[j]:
            i += 1
            j += 1
        # 대문자, 소문자인 경우
        elif a[i].isupper() and b[j].islower():
            return a[i].upper() <= b[j].upper()
        # 소문자, 대문자인 경우
        elif a[i].islower() and b[j].isupper():
            return a[i].upper() < b[j].upper()
        # 숫자, 문자 or 문자, 숫자 or 대문자, 대문자, 소문자, 소문자인 경우
        else:
            return a[i] < b[j]
    return len(a)-i <= len(b)-j

# merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    merged_strings = []
    l = h = 0
    while l < len(low) and h < len(high):
        if natural_sort(low[l], high[h]):
            merged_strings.append(low[l])
            l += 1
        else:
            merged_strings.append(high[h])
            h += 1

    merged_strings += low[l:]
    merged_strings += high[h:]

    return merged_strings

# merge sort를 이용하여 정렬
strings = merge_sort(strings)

for string in strings:
    print(''.join(string))