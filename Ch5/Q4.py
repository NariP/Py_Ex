# Q4 filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

a = list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
print(a)

b = type(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
print(b)
# filter의 결과값은 필터인듯.. 리스트로 보려면 위처럼 리스트 처리를 해줘야하는 듯..
# 수련이 더 필요한 걸로..