
n = int(input())
array = [0 for _ in range(n)]
answer = [[0] * n for _ in range(n)]

for i in range(n):
    array[i] = list(map(str, input()))


for i in range(n):
    for j in range(n):
        count = 0
        if array[i][j] != '.':
            answer[i][j] = "*"
        else:
            # 상
            if i - 1 >= 0:
                if array[i - 1][j] != ".":
                    count += int(array[i - 1][j])
                # 좌측 상
                if j - 1 >= 0:
                    if array[i - 1][j - 1] != ".":
                        count += int(array[i - 1][j - 1])
                # 우측 상
                if j + 1 <= n - 1:
                    if array[i - 1][j + 1] != ".":
                        count += int(array[i - 1][j + 1])

            # 하
            if i + 1 <= n - 1:
                if array[i + 1][j] != ".":
                    count += int(array[i + 1][j])
                # 좌측 하
                if j - 1 >= 0:
                    if array[i + 1][j - 1] != ".":
                        count += int(array[i + 1][j - 1])
                # 우측 하
                if j + 1 <= n - 1:
                    if array[i + 1][j + 1] != ".":
                        count += int(array[i + 1][j + 1])

            # 좌
            if j - 1 >= 0:
                if array[i][j - 1] != ".":
                    count += int(array[i][j - 1])

            # 우
            if j + 1 <= n - 1:
                if array[i][j + 1] != ".":
                    count += int(array[i][j + 1])

            if count >= 10:
                answer[i][j] = "M"
            else:
                answer[i][j] = count

for i in range(n):
    for j in range(n):
        print(answer[i][j], end='')
    print()