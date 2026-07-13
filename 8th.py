priority = [2, 5, 1, 4, 3]
n = len(priority)

for i in range(n):
    for j in range(n - i - 1):
        if priority[j] < priority[j + 1]:

            temp = priority[j]
            priority[j] = priority[j + 1]
            priority[j + 1] = temp
            print(priority)
            print("Emergency Queue")





















