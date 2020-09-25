# 백준 이름궁합 테스트
# https://www.acmicpc.net/problem/17269

#M = 8
#N = 14
#A = "LEESIYUN"
#B = "MIYAWAKISAKURA"

M = 8
N = 12
A = "PARKNARI"
B = "KIMBYEONGHUN"

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ''
min_len = min(M, N)
max_len = max(M, N)

for i in range(min_len):
    AB += A[i] + B[i]
AB += A[min_len:] + B[min_len:]

lst = [alp[ord(i)-ord('A')] for i in AB]

while (len(lst) > 2):
    temp =[]
    for i in range(len(lst)-1):
        sum = lst[i] + lst[i+1]
        if sum >= 10:
            sum -= 10
        temp.append(sum)
    lst.clear()
    lst = temp

print(lst)
print("궁합은 {}%".format(lst[0]*10 + lst[1]))

# temp가 while문 반복의 수 만큼 생성되어 메모리가 낭비될 것이라고 예상됨!ㅋㅋㅋㅋ
