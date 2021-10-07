def calc_line(x, y):
    return (x ** 2 + y ** 2) ** 0.5


x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
isTrue = True
if x_a == x_b:
    if x_b == x_c:
        print(-1.0)
        isTrue = False
    else:
        isTrue = True

elif y_c == (y_b - y_a) / (x_b - x_a) * (x_c - x_a) + y_a:
    print(-1.0)
    isTrue = False

if isTrue:
    ab = calc_line(x_a - x_b, y_a - y_b)
    ac = calc_line(x_a - x_c, y_a - y_c)
    bc = calc_line(x_b - x_c, y_b - y_c)

    print((max(ab, ac, bc) - min(ab, ac, bc)) * 2)