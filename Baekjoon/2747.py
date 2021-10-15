"""def fib(n):
    curr, next = 0, 1
    for _ in range(n):
        curr, next = next, curr + next
    return curr

print(fib(int(input())))

"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(int(input())))