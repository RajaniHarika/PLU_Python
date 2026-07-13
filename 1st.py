roll = [10, 20, 30, 40, 50]

x = int(input("Enter Roll Number: "))

found = False

for i in range(len(roll)):
    if roll[i] == x:
        print("Student Found at position", i)
        found = True
        break

if not found:
    print("Student Not Found")




