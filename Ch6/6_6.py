# 6_6 특정디렉터리의 하위파일 중 파이썬 파일만 출력해주는 프로그램
import os

for (path, dir, files) in os.walk("c:/Users/nrp/Documents/Py_Ex/Ch6"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))