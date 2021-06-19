import datetime


def solution(a, b):
    answer = ''
    t = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = t[datetime.date(2016, a, b).weekday()]

    return answer


print(solution(5, 24))
