order1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2, 3, 4]
order2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2, 3, 5]
order3 = ["XYZ", "XWY", "WXA"]
course3 = [2, 3, 4]

def solution(orders, course):
    answer = []
    orders = sorted(orders, key=len)
    #print(orders)
    candiates = []
    real_menu = []
    for num in course:
        for order in orders:
            if len(order) == num:
                candiates.append(order)
    #print(candiates)
    for candiate in candiates:
        menu = []
        #print(candiate)
        for order in orders:
            if candiate in order:
                menu.append(order)
        #print(menu)
        if len(menu) >= 2:
            real_menu.append(candiate)
    answer = sorted(real_menu)
    return answer

print("================")
res = solution(order1, course1)
print(res)