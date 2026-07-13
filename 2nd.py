product = [10, 20, 30, 40, 50]
x = int(input("Enter Product ID: "))
low = 0
high = len(product) - 1
while low <= high:
    mid = (low + high) // 2
    if product[mid] == x:
        print("Product Found at index", mid)
        break
    elif product[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Product Not Available")




