# 프로그래머스 완주하지 못한 선수 - hash 이용
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
        print(temp)

    return answer

print(solution(participant, completion))

# 대신 해시값 충돌 나면 에러남

