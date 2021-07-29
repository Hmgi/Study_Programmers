N = input()
# 앞자리가 1일때 10인지 1인지 판별
if len(N) == 2:
    print(int(N[0]) + int(N[1]))
elif len(N) == 3:
    if N[1] == str(0):
        print(10 + int(N[2]))
    elif N[2] == str(0):
        print(10 + int(N[0]))
else:
    print(20)
