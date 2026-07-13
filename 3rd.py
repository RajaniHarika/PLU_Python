marks = [65, 80, 45, 90, 70]
n = len(marks)
for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]
print(marks)

