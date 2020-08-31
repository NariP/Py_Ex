# 페이징 하기
# 함수 이름은? getTotalPage
# 입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값은? 총 페이지수

def getTotalPage(m, n):
    if m % n == 0:
        print(m/n)
    else:
        print(m//n + 1)

getTotalPage(5, 10)