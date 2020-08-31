# https://wikidocs.net/42528
# Q7 다음과 같은 내용을 지닌 파일 test3.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

with open("test3.txt", "r") as f:
    body = f.read()

body = body.replace('java', 'python')

with open("test3.txt", "w") as f1:
    f1.write(body)