def solution(record):
    answer = []
    dic = {}
    for i in record:
        uid = i.split(" ")
        dic[uid[1]] = uid[2]

    print(dic)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo"]))
