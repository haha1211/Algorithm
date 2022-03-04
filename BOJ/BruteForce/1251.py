# 1251.단어 나누기

words = input()
n = len(words)

# Brute Force
# 세 단어로 나눌 수 있는 모든 경우의 수 구하기
brute = []
for x in range(n-2):
    for y in range(x+1, n-1):
        # 각각 뒤집고 합치기
        result = words[x::-1] + words[y:x:-1] +words[:y:-1]
        brute.append(result)

# 정렬 후 사전순으로 가장 앞서는 단어 출력
brute.sort()
print(''.join(brute[0]))

    
