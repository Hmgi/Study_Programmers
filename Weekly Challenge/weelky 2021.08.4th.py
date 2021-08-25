def solution(table, languages, preference):
    lang_temp = {}
    max_score = 0
    max_index = 0
    for i in range(len(table)):
        languages_sum = 0
        temp = table[i].split(" ")
        temp.reverse()

        for jdx, j in enumerate(languages):
            for lan in temp[:5]:
                if j == lan:
                    languages_sum += (temp.index(j) + 1) * preference[jdx]
        lang_temp[temp[5]] = languages_sum
    lang_temp = sorted(lang_temp.items(), key=lambda x: (x[0], x[1]))
    for pdx, p in enumerate(lang_temp):
        if max_score < p[1]:
            max_score = p[1]
            max_index = pdx
    return lang_temp[max_index][0]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
