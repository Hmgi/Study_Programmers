x, y = map(int, input().split())
if x == y and x != 0:
    print("Even %d" % (x * 2))
elif x == 0 and y == 0:
    print("Not a moose")
else:
    print("Odd %d" % (max(x, y) * 2))