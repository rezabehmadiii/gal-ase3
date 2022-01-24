
Scores = []

while True:
    score = float(input())
    if score == -1:
        break
    Scores.append(score)

average = sum(Scores) / len(Scores)
print(average)
