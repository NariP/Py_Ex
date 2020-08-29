# https://wikidocs.net/42526
# Q4 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.

pin = "881120-1068234"

print(pin[7])

if int(pin[7]) == 1:
    print("man")
else:
    print("woman")