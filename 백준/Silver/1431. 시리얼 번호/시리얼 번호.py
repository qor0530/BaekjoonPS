from heapq import heappop, heappush

n = int(input())
word = [input() for _ in range(n)]
hq = []
for i in range(n):
    score = 0
    for j in range(len(list(word[i]))):
        if word[i][j].isdigit():
            score += int(word[i][j])
    heappush(hq, (len(word[i]), score, word[i]))

for i in range(n):
    _, _, w = heappop(hq)
    print(w)