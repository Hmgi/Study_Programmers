t, p = map(int, input().split())
if p >= 20:
    use = t / (100 - p)
    print(use * (p - 20) + use * 2 * 20)
else:
    use = t / (120 - 2 * p)
    print(use * 2 * p)