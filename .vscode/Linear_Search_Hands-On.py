# Initialize an empty list to store the numbers
numbers = []

# Continuously ask for numbers until -1 is entered
while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    numbers.append(num)

# Ask for the number to be searched
search_num = int(input("What number would you like to search? "))

# Use linear search to find the number
for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(f"{search_num} found at index {i}")
        break
else:
    print(f"{search_num} not found in the list")