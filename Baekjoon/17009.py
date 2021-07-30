A_count, B_count = 0, 0
for i in range(3, 0, -1):
    A_count += int(input()) * i
for i in range(3, 0, -1):
    B_count += int(input()) * i
print("A" if A_count > B_count else "B" if A_count < B_count else "T")