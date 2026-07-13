time = [25, 12, 19, 10, 30]
for i in range(1, len(time)):
    key = time[i]
    j = i - 1
    while j >= 0 and time[j] > key:
        time[j + 1] = time[j]
        j -= 1
    time[j + 1] = key
    print(time)




