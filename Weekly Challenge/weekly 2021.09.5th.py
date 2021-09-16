from itertools import product


def solution(word):
    word_list = ["A", "E", "I", "O", "U"]
    dict = []

    for index in range(1, 6):
        for i in product(word_list, repeat=index):
            dict.append(i)

    answer_dict = [''.join(words) for words in dict]

    answer_dict.sort()

    for idx, i in enumerate(answer_dict):
        if i == word:
            return idx + 1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

