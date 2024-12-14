def binary_search_iterative(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def main():
    numbers = []
    while True:
        num = int(input("Enter number: "))
        if num == -1:
            break
        numbers.append(num)

    numbers.sort()
    print("Sorted numbers:", *numbers)

    target = int(input("What number would you like to search? "))
    index = binary_search_iterative(numbers, target)
    if index == -1:
        print(f"{target} not found in the list.")
    else:
        print(f"{target} found at index {index}")

if __name__ == "__main__":
    main()
