a, b, c = map(int, input().split())
a_1, b_1, c_1 = map(int, input().split())

if a_1 >= a and b_1 >= b and c_1 >= c:
    print("A")

elif a_1 >= a / 2 and b_1 >= b and c_1 >= c:
    print("B")

elif b_1 >= b and c_1 >= c:
    print("C")

elif b_1 >= b / 2 and c_1 >= c / 2:
    print("D")

else:
    print("E")