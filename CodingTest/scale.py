# 백준 음계
# https://www.acmicpc.net/problem/2920

input1 = [1, 2, 3, 4, 5, 6, 7, 8]
input2 = sorted(input1, reverse=True)
input3 = [8, 1, 7, 2, 6, 3, 5, 4]
inputs = [input1, input2, input3]

scale = [i for i in range(1, 9)]


def is_sort(input):
    if input == scale:
        print('ascending')
    elif input == sorted(scale, reverse=True):
        print("descending")
    else:
        print("mixed")


for input in inputs:
    print("== input1 ==")
    is_sort(input)

def is_sort2(input):
    ascending = True
    descending = True
    for i in range(7):
        if input[i] < input[i+1]:
            descending = False
        elif input[i] > input[i+1]:
            ascending = False
    return ascending, descending

print("=========================")
for input in inputs:
    asc, desc = is_sort2(input)
    if asc == True:
        print("ascending")
    elif desc == True:
        print("descending")
    else:
        print("mixed")
