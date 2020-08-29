# https://wikidocs.net/42526
# Q9 오류가 발생하는 것을 고르시오

a = dict()
print(a)

#1 a['name'] = 'python'
#2 a[('a',)] = 'python'
#3 a[[1]] = 'python' 딕셔너리의 key는 불변값만 가능한데, list는 값이 변할 수 있으니 안 된다
#4 a[250] = 'python'

a['name'] = 'python'
print("1. ", a)

a[('a',)] = 'python'
print("2. ", a)

a[250] = 'python'
print("4. ", a)