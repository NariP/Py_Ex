# https://wikidocs.net/42528
# Q6 사용자의 입력을 파일(test1.txt)에 저장하는 프로그램을 작성해 보자.
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

with open("test1.txt","a") as file:
    data = input("입력: ")
    file.write(data+"\n")