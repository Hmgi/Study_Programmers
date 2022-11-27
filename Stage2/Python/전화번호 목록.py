def solution(phone_book):
    phoneBook = sorted(phone_book)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
    return True


print(solution(["119", "97674223", "1195524421"]))
