string_dict = ["/", "-", "\\", "(", "@", "?", ">", "&", "%"]
while True:
    string = input()
    string_len = len(string)
    answer = 0
    if string == "#":
        break
    for i in string:
        answer += (string_dict.index(i) - 1) * (8 ** (string_len - 1))
        string_len -= 1
    print(answer)