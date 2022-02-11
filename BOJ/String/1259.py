# 1259.팰린도름수

while True:
    n = input()
    # 입력 종료
    if n == "0":
        break
    flag = True

    # 팰린드롬 확인
    # 반까지만 확인하면 됨
    # 끝까지 확인하면 중복 -> 시간 낭비
    for i in range(len(n)//2):
        if n[i] == n[len(n)-1-i]:
            continue
        else:
            flag = False
            break

    if flag:
        print("yes")
    else:
        print("no")