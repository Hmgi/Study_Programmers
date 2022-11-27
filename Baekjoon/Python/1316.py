def check_word(words):
    answer = []
    for i in range(len(words)):
        if i == 0:
            answer.append(words[i])
        else:
            if words[i] != words[i-1]:
                if words[i] in answer:
                    return False
                else:
                    answer.append(words[i])
    return True


n = int(input())
count = 0
for _ in range(n):
    word = input()
    if check_word(word):
        count += 1
print(count)