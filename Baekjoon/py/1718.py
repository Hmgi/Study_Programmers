string = input()
key = input()
answer = ''
alph_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key_index = 0
for i in string:
    if i == " ":
        answer += " "
        key_index += 1
    else:
        temp = ord(i) - alph_dict.index(key[key_index]) - 1
        if temp < 97:
            temp += 26
        answer += chr(temp)
        key_index += 1
    if key_index == len(key):
        key_index = 0
print(answer)