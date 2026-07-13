book = [101,102,103,104,105,106,107,108]
num = int(input("Enter Book ID: "))
low = 0
high = len(book) - 1
while low <= high:
    mid = (low + high) // 2
    if book[mid] == num:
        print("Book Found at Index", mid)
        break
    elif book[mid] < num:
        low = mid + 1
    else:
        high = mid - 1
        if low > high:
            print("Book Not Found")


    