salary1 = [25000, 30000, 28000]
salary2 = [26000, 35000, 27000]

salary = salary1 + salary2

n = len(salary)

for i in range(n):
    for j in range(n - i - 1):

        if salary[j] > salary[j + 1]:

            temp = salary[j]
            salary[j] = salary[j + 1]
            salary[j + 1] = temp

print("Salary List")
print(salary)