# Q12 time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# 2018/04/03 17:20:32

import time

#print(time.localtime(time.time()))
#print(time.asctime(time.localtime(time.time())))
#print(time.ctime())
#year = time.strftime('%Y', time.localtime(time.time()))
#month = time.strftime('%m', time.localtime(time.time()))
#day = time.strftime('%d', time.localtime(time.time()))
#time = time.strftime('%X', time.localtime(time.time()))
#print(year+"/"+month+"/"+day+" "+time)
all_time = time.strftime("%Y/%m/%d %H:%M:%S")
print(all_time)