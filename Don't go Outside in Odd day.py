# Get input from the user
numbers = input("Enter a series of numbers: ")

# Split the input string into a list of numbers
numbers_list = numbers.split()

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

#Iterate through the numbers and count even and odd numbers
for num in numbers_list:
    num = int(num)  # Convert the string to an integer
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

#Print the results
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
