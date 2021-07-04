# 2진수 변환함수
def transNum(n, arr):
    transN = list()
    for i in range(n):
        if arr % 2 == 0 or arr <= 0:
            transN += '0'
        else:
            transN += '1'
        arr = int(arr / 2)
    transN.reverse()
    return transN


def solution(n, arr1, arr2):
    answer = []
    arr1List = list()
    arr2List = list()

    for i in range(n):
        answerString = ''
        
        # 2진수 변환 함수를 통해 각각 List로 받아와 1이 있는지 없는지 비교
        arr1List = transNum(n, arr1[i])
        arr2List = transNum(n, arr2[i])

        for j in range(n):
            if arr1List[j] == '1' or arr2List[j] == '1':
                answerString += "#"
            else:
                answerString += " "

        answer.append(answerString)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
