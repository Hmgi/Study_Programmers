def T(number):
    number_sum = 0
    for i in range(1, number+1):
        number_sum += i
    return number_sum


t = int(input())
for _ in range(t):
    n = int(input())
    print(sum([k * T(k+1) for k in range(1, n+1)]))
