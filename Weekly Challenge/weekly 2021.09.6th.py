def solution(weights, head2head):
    user_info = []

    for user in range(len(weights)):
        over_weights = [i for i in range(len(weights)) if weights[user] < weights[i]]
        over_win = 0
        for i in over_weights:
            if head2head[user][i] == "W":
                over_win += 1
        if len(head2head[user]) - head2head[user].count("N") == 0:
            rating = 0
        else:
            rating = round(head2head[user].count("W") / (len(head2head[user]) - head2head[user].count("N")) * 100, 2)
        user_info.append((user, weights[user], over_win, rating))
        user_info = sorted(user_info, key=lambda x: (x[3], x[2], x[1], -x[0]), reverse=True)
    return [i[0] + 1 for i in user_info]


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
# print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))

'''
over_weights = []
        for i in range(len(weights)):
            if weights[user] < weights[i]:
                over_weights.append(i)
'''