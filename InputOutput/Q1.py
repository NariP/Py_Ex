# https://wikidocs.net/42528
# Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd(num):
    if num % 2:
        print("홀수")
    else:
        print("짝수")

is_odd(3)
is_odd(2)