from itertools import combinations as c

phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
phone_book4 = ["12","567","56788"]

def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    print(sortedPB)
    print("{0:=^10}".format(""))
    for (a,b) in c( sortedPB,2):
        print(a,b)
        if a == b[:len(a)]:
            answer = False
    return answer

solution(phone_book3)