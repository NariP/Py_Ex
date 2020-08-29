# https://wikidocs.net/42526
# Q3 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.

pid = "881120-1068234"

print(pid.split("-"))
print("yyyymmdd : ",pid[:6])
print("num : ", pid[7:])