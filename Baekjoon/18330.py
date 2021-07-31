use_g = int(input())
gas = int(input())

if use_g - gas > 60:
    use_g -= 60
    print(gas * 1500 + 60 * 1500 + (use_g - gas) * 3000)
else:
    print(gas * 1500 + (use_g - gas) * 1500)