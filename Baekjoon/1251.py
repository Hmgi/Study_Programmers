string = input()
answer = []

for i in range(len(string) - 2):
    temp1 = string[:i+1]

    for j in range(i + 1, len(string) - 1):
        temp2 = string[i+1:j+1]
        temp3 = string[j+1:]
        print(temp1, temp2, temp3)

        answer.append(temp1[::-1] + temp2[::-1] + temp3[::-1])
print(min(answer))
