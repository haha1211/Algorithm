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
for i in range(max(1,x-(length*9)), x):
    if i + sum(i) == x:
        result = i
        break

print(result)