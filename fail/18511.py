from itertools import product

N, K = map(int, input().split())
k_list = list(map(int, input().split()))

flag = True
k_list.reverse()

length = len(str(N))

while flag:
    result = list(product(k_list, repeat=length))

    for i in result:
        temp = ''.join(map(str, i))
        if N >= int(temp):
            print(temp)
            flag = False
            break
    length -= 1
