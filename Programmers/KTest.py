import re
ex1 = ".d...abc..www.ee"
new_id = "...!@BaT#*..y.abcdefghijklm"
special_character= "/[\{\}\[\]\/?,;:|\)*~`!^+<>@\#$%&\\\=\(\'\"]/g"
special_character2= "/[\{\}\[\]\/?,;:|\)*~`!^+<>@\#$%&\\\=\(\'\"]"

b = "abcd"
c = ""


new_id2 = new_id.lower()
print(new_id2)
p = re.compile("[\{\}\[\]\/?,;:|\)*~`!^+<>@\#$%&\\\=\(\'\"]")
match = re.search(p, new_id2)
print(match)

sub = re.sub(pattern=p, repl='', string=new_id2)
print(sub)

dots_p = "\.\.+"
find_dot = re.search(dots_p, ex1)
if find_dot:
    print("닷 여러개 연속")
    rm_dots = re.sub(pattern=dots_p, repl=".", string=sub)
    print(rm_dots)
else:
    print("연속아님")

if rm_dots.startswith('.'):
    print("처음에 . 있음")
    rm_dots = rm_dots[1:]
    print(rm_dots)
elif rm_dots.endswith('.'):
    print('끝에 .있음')
    rm_dots = rm_dots[:-1]
    print(rm_dots)
else:
    print('pass')

if len(rm_dots) >= 16:
    print("16자 이상")
    rm_dots = rm_dots[:15]
else:
    print("pass")

if rm_dots.endswith('.'):
    print('끝에 .있음')
    rm_dots = rm_dots[:-1]
else:
    print("pass")
print(rm_dots)