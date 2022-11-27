N = int(input())
i = 2
while N != 1:
    if N % i == 0:
        print(i)
        N /= i
    else:
        i += 1

#########################
n = int(input())
while True:
    if n % 2 == 0:
        n /= 2
        print(2)
    else:
        break
x = int(n)
for i in range(3, x+1, 2):
    while True:
        if n % i == 0:
            n /= i
            print(i)
        else:
            break
