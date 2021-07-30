import math
A, P_1 = map(int, input().split())
R, P_2 = map(int, input().split())
if A / P_1 > R ** 2 * math.pi / P_2:
    print("Slice of pizza")
else:
    print("Whole pizza")