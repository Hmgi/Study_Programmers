'''
N, M = map(int, input().split())
d = []
answer = []
for _ in range(N):
    d.append(input())
for _ in range(M):
    name = input()
    if name in d:
        answer.append(name)

print(len(answer))
for i in answer:
    print(i)
'''
N, M = map(int, input().split())
N_list = []
M_list = []
for _ in range(N):
    N_list.append(input())
for _ in range(M):
    M_list.append(input())

dup = list(set(N_list) & set(M_list))
print(len(dup))
for i in sorted(dup):
    print(i)