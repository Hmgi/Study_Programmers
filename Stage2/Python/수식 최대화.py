import itertools


def calc_number(a, b, obj):
    if obj == "+":
        return str(int(a) + int(b))
    elif obj == "-":
        return str(int(a) - int(b))
    elif obj == "*":
        return str(int(a) * int(b))


def solve_number(arr, comb):
    arr_temp = arr.copy()
    for i in comb:
        stack = []
        while len(arr_temp) != 0:
            temp = arr_temp.pop(0)
            # 기호가 같을 때
            if temp == i:
                stack.append(calc_number(stack.pop(), arr_temp.pop(0), temp))
            else:
                stack.append(temp)
        arr_temp = stack
    return abs(int(arr_temp[0]))


def solution(expression):
    answer = []
    stack = []
    temp = ""

    for i in expression:
        if i.isdigit():
            temp += i
        else:
            stack.append(temp)
            stack.append(i)
            temp = ""
    stack.append(temp)

    calc = ["+", "-", "*"]
    calc = list(itertools.permutations(calc, 3))

    for i in calc:
        answer.append(solve_number(stack, i))
    return max(answer)


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
