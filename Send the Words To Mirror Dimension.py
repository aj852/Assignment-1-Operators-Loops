# Define a function to reverse a word
def reverse_word(word):
    return word[::-1]

# Get input from the user
word = input("Enter a word: ")

# Call the reverse_word function and print the reversed word
reversed_word = reverse_word(word)
print("Reversed word:", reversed_word)
