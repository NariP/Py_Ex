# https://wikidocs.net/42528
# Q2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# ※ 평균 값을 구할 때 len 함수를 사용해 보자.

def avg_numbers(*args):
    print(type(args))
    return sum(args) / len(args)

print(avg_numbers(1,2,3))