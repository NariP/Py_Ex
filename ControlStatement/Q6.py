# https://wikidocs.net/42527
# Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

# 위의 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자
print("{0:=^10}".format("리스트 내포"))

numbers2 = [1, 2, 3, 4, 5]
result2 = [n*2 for n in numbers2 if n%2==1]
print(result2)