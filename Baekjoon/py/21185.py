N = int(input())
if N % 2 != 0:
    print("Either")
elif N % 2 == 0:
    if N / 2 % 2 == 0:
        print("Even")
    else:
        print("Odd")