def solution(genres, plays):

    answer = []
    play_Dict = {}
    d = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in play_Dict:
            play_Dict[genre] += play
        else:
            play_Dict[genre] = play

        d[genre] = d.get(genre, []) + [[play, i]]

    genreSort = sorted(play_Dict.items(), key=lambda x: x[1], reverse=True)

    for (genre, totalPlay) in genreSort:
        d[genre] = sorted(d[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in d[genre][:2]]

    return answer


print(solution(["classic", "classic", "classic", "pop"], [500, 150, 800, 2500]))
