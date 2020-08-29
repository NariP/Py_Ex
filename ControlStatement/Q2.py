# https://wikidocs.net/42527
# Q2 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

sum = 0
a = range(1, 1001)
for item in a:
    if item % 3:
        pass
    else:
        sum += item

print(sum)

print("{0:=^10}".format("while문 써서 하기"))

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) # 166833 출력