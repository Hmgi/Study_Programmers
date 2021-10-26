i = 1
while True:
    d, r, t = map(float, input().split())

    if r == 0:
        break

    distance = d / 63360 * 3.141592 * r

    mph = distance / t * 3600

    print("Trip #%d: %.2f %.2f" %(i, distance, mph))
    i += 1