score = [200, 500, 300, 700, 400]

n = len(score)

for i in range(n):
    for j in range(n - i - 1):

        if score[j] < score[j + 1]:

            temp = score[j]
            score[j] = score[j + 1]
            score[j + 1] = temp

print("Leaderboard")
print(score)