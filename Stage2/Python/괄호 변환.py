def divide(string):
    open_count = 0
    close_count = 0

    for i in range(len(string)):
        if string[i] == "(":
            open_count += 1
        else:
            close_count += 1

        if open_count == close_count:
            return string[:i+1], string[i+1:]


def check(string):
    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    if not p:
        return ""

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"

        u = u[1:len(u)-1]
        for i in u:
            if i == "(":
                answer += ")"
            else:
                answer += "("

        return answer


print(solution("()))((()"))
