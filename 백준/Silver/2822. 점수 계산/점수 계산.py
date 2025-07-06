score = []

for i in range(1, 9):
    score.append(int(input()))

sorted_score = sorted(score, reverse=True)

seq = []

for i in range(5):
    seq.append(score.index(sorted_score[i])+1)

seq.sort()

print(sum(sorted_score[:5]))
print(seq[0], seq[1], seq[2], seq[3], seq[4])