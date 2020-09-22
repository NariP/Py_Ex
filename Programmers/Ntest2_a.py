ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

def solution(ball, order):
    new_order = []
    hold_items = []
    for num in order:
        print(num, ball[0], ball[-1])
        if num == ball[0] or num == ball[-1]:
            print('{0} 들어감'.format(num))
            new_order.append(num)
            del ball[ball.index(num)]
            for item in hold_items:
                if item == ball[0] or item == ball[-1]:
                    new_order.append(item)
                    del ball[ball.index(item)]
                    del hold_items[hold_items.index(item)]
                    print("보류되었던 {0} 들어감".format(item))
        else:
            hold_items.append(num)
            print('{0} 보류'.format(num))
        print("보류된 것들 : ", hold_items)
    answer = new_order
    return answer

print(solution(ball, order))