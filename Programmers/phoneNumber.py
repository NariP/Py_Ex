phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
phone_book4 = ["12","567","56788"]

print(min(phone_book1))

def solution(phone_book):
    answer = True
    return answer

wantSplit = 3

print(len(phone_book1[1])//wantSplit+1)
print('{0:=^10}'.format("="))

for i in range(len(phone_book1[1])//wantSplit+1):
    if i == 0:
        "".join(phone_book1[1][0:i + wantSplit])
        start = 0+wantSplit
    else:
        "".join(phone_book1[1][start:wantSplit*i])
        start += wantSplit

a = []
for i in range(len(phone_book1[1])//wantSplit+1):
    if i != 0:
        start += wantSplit
        end_index = wantSplit + wantSplit * i
    else:
        start = 0
        end_index = wantSplit
    a.append("".join(phone_book1[1][start:end_index]))


print(a)