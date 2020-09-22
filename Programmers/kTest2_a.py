order1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2, 3, 4]
order2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2, 3, 5]
order3 = ["XYZ", "XWY", "WXA"]
course3 = [2, 3, 4]

def solution(orders, course):
    answer = []
    orders = sorted(order1, key=len)
    print(orders)
    for num in course:
        menu = []
        pick = ''
        for (index, order) in enumerate(orders):
            print("pick 길이 : ", len(pick))
            if len(order) == num:
                pick = order
                print("코스 명 : ", pick)
            if pick in order:
                menu.append(order)
        print(menu)
        orders.pop(0)
        print("확인하기")
        print(orders)
        print("{0:=^10}".format("="))
    return answer

solution(order1, course1)