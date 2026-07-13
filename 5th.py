price = [10, 20, 30, 40]
new = int(input("Enter New Price: "))
price.append(new)

for i in range(1, len(price)):
    key = price[i]
    j = i - 1
    while j >= 0 and price[j] > key:
        price[j + 1] = price[j]
        j -= 1
    price[j + 1] = key

print(price)















