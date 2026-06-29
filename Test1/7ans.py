#7.	Create student.txt, write your name, then read and display it.
f = open("student.txt", "w")
f.write("koushik")
f.close()

f = open("student.txt", "r")
print(f.read())
f.close()