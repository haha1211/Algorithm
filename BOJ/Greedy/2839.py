n = int(input())

total = 0
while n:
    if n % 5 == 0:
        total += n // 5
        break
    n -= 3
    total += 1

if n < 0 : 
    total = -1

print(total)
