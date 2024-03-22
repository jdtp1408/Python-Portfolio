# This defines a function that is intended to slice the first 5 characters of a user input string
def first_five_characters():
    user_input = input("Please enter the string you want sliced. This function will print the first 5 characters: ")
    print(user_input[1:5])

# The incorrect indices make the output incorrect, even though the code runs.
first_five_characters()

