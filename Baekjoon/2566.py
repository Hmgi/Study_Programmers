arr = [i for i in range(9)]
answer = []
for i in range(9):
    arr[i] = list(map(int, input().split()))
    answer.append(max(arr[i]))
print(max(answer))

print(answer.index(max(answer)) + 1, arr[answer.index(max(answer))].index(max(answer)) + 1)
