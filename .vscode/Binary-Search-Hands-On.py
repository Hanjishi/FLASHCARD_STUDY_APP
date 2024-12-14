def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

numbers = []
while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    numbers.append(num)

numbers.sort()
print("Sorted numbers:", *numbers)

search_num = int(input("What number would you like to search? "))

result = binary_search(numbers, 0, len(numbers)-1, search_num)

if result != -1:
    print(search_num, "found at index", result)
else:
    print(search_num, "not found in the list")