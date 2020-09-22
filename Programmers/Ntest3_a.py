n = 9
n1 = 73425
n2 = 10007

def solution(n):
    str_n = str(n)
    count_plus = 0
    res = 0
    if len(str_n) == 1:
        res = n
    else:
        while len(str_n) != 1:
            count_plus += 1
            print(len(str_n))
            if len(str_n) < 3:
                res = int(str_n[0]) + int(str_n[1])
                str_n = str(res)
            else:
                type1 = int(len(str_n) / 2)
                type2 = int(len(str_n) / 2) + 1
                print(str_n[type1:], str_n[type2:])
                if str_n[type1:] or str_n[type2:] == "0":
                    print("여기냐?")
                    res3 = int(float(str_n[type2:])) + (int(float(str_n)) - int(float(str_n[type2:])))
                    str_n = str(res3)
                else:
                    print("여기로 갔음")
                    res1 = int(float(str_n[:type1])) + int(float(str_n[type1:]))
                    res2 = int(float(str_n[:type2])) + int(float(str_n[type2:]))
                    if res1 < res2:
                        str_n = str(res1)
                    else:
                        str_n = str(res2)

    answer = [count_plus, res]
    return answer

print(solution(n1))

