# 6_4
# 원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.
# 필요한 기능은? 메모 추가하기, 메모 조회하기
# 입력 받는 값은? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은? memo.txt

def validate_option(op):
    option_list = ['r', 'w', 'a']
    if op not in option_list:
        print("옵션의 종류: ", option_list)
        print("option 값이 아닙니다 다시 입력하세요^^")
        return False
    else:
        return True

def memo_exe(op, data):
    if op == 'r':
        with open("memo.txt", 'r') as f:
            print(f.read())
    elif op == 'w':
        with open("memo.txt", 'w') as f:
            f.write(data)
            print("작성 되었습니다")
    else:
        with open("memo.txt", 'a') as f:
            f.write(data)
            print("추가되었습니다")

def memo():
    option = input("option: ")
    if validate_option(option):
        if option == 'w' or option == 'a':
            body = input("내용을 입력: ")
            memo_exe(option, body)
        else:
            memo_exe(option, '')
    else:
        memo()




def start():
    while True:
        y_or_n = input("프로그램 실행 y or n? ")
        if y_or_n == 'n':
            print("-- 프로그램을 종료합니다 --")
            break
        elif y_or_n == 'y':
            memo()
        else:
            print("잘못된 값을 입력했습니다.")

if __name__ == "__main__":
    start()