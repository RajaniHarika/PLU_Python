marks = [75,45,90,60,85]
n = len(marks)
for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp
            print(marks)
            print("Sorted Marks")
            num = int(input("Enter Mark: "))
            found = False
            for i in range(len(marks)):
                if marks[i] == num:
                    print("Mark Found at Position", i)
                    found = True
                    break
                if found == False:
                    print("Mark Not Found")


