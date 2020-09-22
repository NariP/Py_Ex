import re
new_id1 = "...!@BaT#*..y.abcdefghijklm"
b = "..!$bas"

def solution(new_id):
    # 대문자 > 소문자
    if new_id.islower():
        print("1단계 : 변화가 없습니다.")
    else:
        new_id = new_id.lower()
        print(new_id)

    # 특수문자 제거
    p = re.compile("[\{\}\[\]\/?,;:|\)*~`!^+<>@\#$%&\\\=\(\'\"]")
    search = re.search(p, new_id)
    if search:
        new_id = re.sub(pattern=p, repl='', string=new_id)
        print(new_id)
    else:
        print("2단계 : 변화가 없습니다.")

    # .여러개 1개로 수정
    dots_p = "\.\.+"
    find_dot = re.search(dots_p, new_id)
    if find_dot:
        print("닷 여러개 연속")
        new_id = re.sub(pattern=dots_p, repl=".", string=new_id)
        print(new_id)
    else:
        print("3단계 : 변화가 없습니다")

    # 아이디 처음과 끝에 위치한 . 제거
    if new_id.startswith('.'):
        new_id = new_id[1:]
    elif new_id.endswith('.'):
        new_id = new_id[:-1]
    else:
        print("4단계 : 변화가 없습니다.")

    # 빈문자열이면 a 추가
    if len(new_id):
        print("5단계: 변화가 없습니다")
    else:
        new_id = "a"
    # 6단계 : 글자수 줄이기 + 마침표 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]

    if new_id.endswith('.'):
        new_id = new_id[:-1]
    else:
        print("6단계 : 변화가 없습니다.")

    # 7단계 : 글자 수 2자 이하라면 글자수 추가
    if len(new_id) <= 3:
        num = 3 - len(new_id)
        endChar = new_id[-1]
        for i in range(num):
            new_id = new_id + endChar
    else:
        print("7단계 : 변화가 없습니다.")

    answer = new_id

solution(new_id1)