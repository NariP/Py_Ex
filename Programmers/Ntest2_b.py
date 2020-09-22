ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

def solution(ball, order):
    new_order = []
    while order:
        for num in order:
            print(num, order)
            if num == ball[0] or num == ball[-1]:
                new_order.append(num)
                del ball[ball.index(num)]
                del order[order.index(num)]
                break
    answer = new_order
    return answer

print(solution(ball, order))