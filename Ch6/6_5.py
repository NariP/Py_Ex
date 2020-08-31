# 6_5 문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸어 주기
# 필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
# 입력 받는 값은? 탭을 포함한 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일

with open('tabto4.txt', 'w') as f:
    f.write("life\tis\ttoo\tshort\t.")

with open('tabto4.txt', 'r') as fr:
    data = fr.read()
    print(data)

with open('tabto4.txt', 'w') as fw:
    changed_data = data.replace('\t', '_')
    fw.write(changed_data)