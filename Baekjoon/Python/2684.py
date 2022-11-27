n = int(input())

for _ in range(n):
    answer = dict(TTT=0, TTH=0, THT=0, THH=0, HTT=0, HTH=0, HHT=0, HHH=0)
    coin = input()

    for i in range(0, len(coin) - 2, 1):
        answer[coin[i:i+3]] += 1

    for i in list(answer.values()):
        print(i, end=' ')
    print()