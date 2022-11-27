def transNum(num):
    temp = int(num[0]) + int(num[1])

    if len(str(temp)) == 1:
        trans = num[1] + str(temp)
    else:
        temp = str(temp)
        trans = num[1] + temp[1]
    return trans


number = input()
count = 0

if len(number) == 1:
    number = "0" + number
answer = number
while True:
    count += 1
    answer = transNum(answer)
    if number == answer:
        print(count)
        break
