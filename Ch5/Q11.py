# Q11 glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.

import glob

path = "./*"

file_list = glob.glob(path)
file_list_py = [file for file in file_list if file.endswith(".py")]

print("file_list_py: {}".format(file_list_py))

print(glob.glob("./*.py"))

# 출력은 자동으로 되는게 아니다ㅋㅋㅋㅋㅋㅋㅋ