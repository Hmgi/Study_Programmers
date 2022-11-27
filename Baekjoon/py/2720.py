n = int(input())

for _ in range(n):
    money = int(input())
    quarter = money // 25
    money = money % 25

    dime = money // 10
    money = money % 10

    nickel = money // 5
    penny = money % 5

    print(quarter, dime, nickel, penny)