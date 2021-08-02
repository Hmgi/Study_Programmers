def computer_number(testcase, b):
    if testcase == 1 or testcase == 5 or testcase == 6:
        return testcase

    elif testcase == 0:
        return 10

    elif testcase == 4 or testcase == 9:
        if b % 2 == 0:
            return (testcase**2) % 10
        else:
            return testcase

    else:
        if b % 4 == 1:
            return testcase
        elif b % 4 == 0:
            return (testcase ** 4) % 10
        else:
            return (testcase ** (b % 4)) % 10


T = int(input())
answer = []
for _ in range(T):
    a, b = map(int, input().split())
    answer.append(computer_number(a % 10, b))

for i in answer:
    print(i)