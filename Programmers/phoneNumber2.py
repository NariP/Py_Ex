phone_book1 = ["119", "97674223", "1195524421"]
phone_book2 = ["123","456","789"]
phone_book3 = ["12","123","1235","567","88"]
phone_book4 = ["12","567","56788"]

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    print(hash_map)
    return answer

solution(phone_book1)