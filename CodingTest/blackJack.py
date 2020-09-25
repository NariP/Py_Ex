# 백준 블랙잭
# https://www.acmicpc.net/problem/2798
# 파이썬은 1초에 2천만건 정도 처리함, 이 문제는 많이 해봐야 천만건이라서 삼중포문으로 풀음

card_len = 10
M = 500
cards = [93,181, 245, 214, 315, 36, 185, 138, 216, 295]

count = 0
res = 0
for i in range(card_len):
    for j in range(i+1, card_len):
        for k in range(j+1, card_len):
            count = cards[i] + cards[j] + cards[k]
            if count <= M and count > res:
                res = count

print(res)
