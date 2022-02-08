# 2231.분해합

n = input()

length = len(n)
x = int(n)

def sum(num):
    ten = 10
    total = 0
    while num > 0:
        total += num % 10
        num //= ten
    return total

result = 0
# X(3) = K + k1+k2+k3 일때
# X(3) - (k1+k2+k3) = K이고 k1+k2+k3의 최댓값이 3*9이므로
# 그 미만의 숫자는 생성자가 될 수 X
# X - (9 * X의 길이) ~ X까지만 탐색하면 됨
for i in range(max(1,x-(length*9)), x):
    if i + sum(i) == x:
        result = i
        break

print(result)
