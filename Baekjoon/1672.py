def changeString(string):
    change = ''
    if string == 'AA' or string == 'CA' or string == 'AC' or string == 'TG' or string == 'GT':
        change = 'A'
    elif string == 'GA' or string == 'AG' or string == 'CC':
        change = 'C'
    elif string == 'GG' or string == 'TA' or string == 'AT' or string == 'CT' or string == 'TC':
        change = 'G'
    elif string == 'CG' or string == 'GC' or string == 'TT':
        change = 'T'
    return change


n = int(input())
dna = input()
while True:
    if len(dna) == 1:
        break
    else:
        dna = dna[:-2] + changeString(dna[-2:])
print(dna)
