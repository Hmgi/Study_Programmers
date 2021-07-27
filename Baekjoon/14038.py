count = 0
for i in range(6):
    wl = input()
    if wl == "W":
        count += 1
if 1 <= count <= 2:
    print(3)
elif 3 <= count <= 4:
    print(2)
elif 5 <= count <= 6:
    print(1)
else:
    print(-1)