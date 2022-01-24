# 9007.카누 선수

import sys
import bisect

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # meet in the middle
    # A,B / C,D 둘로 나눠서 각 2개 반 학생들 모든 경우의 몸무게 합 구하기
    sum_a = []
    sum_b = []
    for i in range(n):
        for j in range(n):
            sum_a.append(A[i]+B[j])
            sum_b.append(C[i]+D[j])

    # binary search를 위한 정렬
    sum_b.sort()
    result = 0
    # 나올 수 없는 근사값으로 설정
    approximate = 10**9

    for sum in sum_a:
        index = bisect.bisect_left(sum_b, k-sum)
        if index < len(sum_b):
            if sum_b[index] == k-sum:
                result = k
                break
            # bisect_left로 찾았을 때 찾고자 하는 값이 없으면 그 값보다 다음으로 큰 값의 index return
            # 범위 내의 index가 return 된 경우 index, index-1 위치의 원소를 비교 후 근사값이 더 작은 값 선택(small)
            else:
                if abs(k-sum-sum_b[index]) < abs(k-sum-sum_b[index-1]):
                    small = sum_b[index]
                else:
                    small = sum_b[index-1]
        # 범위를 벗어난 경우, 마지막 값 선택(small)
        else:
            small = sum_b[len(sum_b)-1]

        # 기존의 가장 작은 근사값과 비교하여 더 작은 값으로 update
        if approximate > abs(k-sum-small):
            approximate = abs(k-sum-small)
            result = sum + small
        elif approximate == abs(k-sum-small):
            result = min(result, sum+small)

    # 결과 출력
    print(result)
       