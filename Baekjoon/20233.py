a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

if T > 30:
    a_cost = a + (T - 30) * x * 21
else:
    a_cost = a

if T > 45:
    b_cost = b + (T - 45) * y * 21
else:
    b_cost = b

print(a_cost, b_cost)