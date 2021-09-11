fir_string = input()
sec_string = input()

count = 0

while True:
    if sec_string in fir_string:
        fir_string = fir_string.replace(sec_string, " ", 1)
        count += 1
    else:
        break
print(count)