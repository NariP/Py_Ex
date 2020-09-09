from itertools import product
from collections import Counter
from functools import reduce

hat = ["yellow_hat", "green_turban"]
eyewear = ["blue_glasses"]
outer = ["jumper", "coat", "pedding"]
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

add_all = product(hat, eyewear, outer)
list_add_all = list(add_all)
print(list_add_all)
print(len(list_add_all))


def solution(clothes):

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

abc = Counter([kind for name, kind in clothes])
print(abc.values())