color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
calc = ""
for i in range(3):
    in_color = input()
    if i != 2:
        calc += str(color.index(in_color))
    else:
        answer = int(calc) * (10 ** color.index(in_color))
print(answer)
