# 프로그래머스 완주하지 못한 선수 - collections 이용
import collections
import numpy as np

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(participant, completion))

print(collections.Counter(participant))
print(collections.Counter(completion))
print(collections.Counter(participant) - collections.Counter(completion))


datas = np.asarray(participant)
iwantit = np.asarray(completion)
print(np.isin(datas, iwantit))