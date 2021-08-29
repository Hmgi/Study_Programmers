N = int(input())
data = list(map(int, input().split()))
answer = 0
data_sum = 0

temp_data = data + data

for idx, i in enumerate(data):
    for j in range(idx, len(temp_data)):
        data_sum += temp_data[j]
        print(data_sum)
        if data_sum == 50:
            answer += 1
            data_sum = 0
            break
        elif data_sum > 50:
            data_sum = 0
            break

print(answer // 2)