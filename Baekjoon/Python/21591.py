w_c, h_c, w_s, h_s = map(int, input().split())
if w_c - w_s > 1 and h_c - h_s > 1:
    print(1)
else:
    print(0)