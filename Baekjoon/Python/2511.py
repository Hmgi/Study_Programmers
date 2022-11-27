a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_win = 0
b_win = 0
temp = "D"

for i in range(10):
    if a[i] > b[i]:
        a_win += 3
        temp = "A"
    elif a[i] < b[i]:
        b_win += 3
        temp = "B"
    else:
        a_win += 1
        b_win += 1

print(a_win, b_win)
if a_win == b_win:
    print(temp)
elif a_win > b_win:
    print("A")
else:
    print("B")
