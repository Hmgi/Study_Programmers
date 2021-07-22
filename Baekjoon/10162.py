T = int(input())
T1 = T//300
T = T - (T//300 * 300)
T2 = T//60
T = T - (T//60 * 60)
T3 = T//10
if T % 10 != 0:
    print(-1)
else:
    print(T1, T2, T3)