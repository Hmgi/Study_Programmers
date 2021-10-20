def solution(info, query):
    answer = []
    info_temp = [[] for _ in range(len(info))]
    for idx, i in enumerate(info):
        info_temp[idx] = i.split()

    for jdx, j in enumerate(query):
        count = 0
        j_temp = [i for i in j.split() if i != "and"]

        for l in range(len(info)):
            if info_temp[l][0] == j_temp[0] or j_temp[0] == "-":
                if info_temp[l][1] == j_temp[1] or j_temp[1] == "-":
                    if info_temp[l][2] == j_temp[2] or j_temp[2] == "-":
                        if info_temp[l][3] == j_temp[3] or j_temp[3] == "-":
                            if int(info_temp[l][4]) >= int(j_temp[4]):
                               count += 1
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue

        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


