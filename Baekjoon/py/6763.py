A = int(input())
B = int(input())
over = B - A

if 1 <= over <= 20:
    cost = 100
elif 21 <= over <= 30:
    cost = 270
elif 31 <= over:
    cost = 500
else:
    cost = 0

if cost == 0:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $" + str(cost) + ".")
