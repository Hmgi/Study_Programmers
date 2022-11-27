n = int(input())
text = list(input())
for _ in range(n-1):
    temp = input()
    for i in range(len(temp)):
        if text[i] != temp[i]:
            text[i] = "?"
print("".join(text))