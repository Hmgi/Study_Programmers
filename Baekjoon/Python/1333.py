n, l, d = map(int, input().split())

music = [True] * ((n * l) + (5 * (n - 1)))

for i in range(n):
    play_time = (l + 5) * i
    for j in range(play_time, play_time + l):
        music[j] = False
answer = 0
while answer < len(music):
    if music[answer]:
        break
    answer += d
print(answer)