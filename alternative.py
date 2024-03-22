# Variable that enscapsulates user input string
user_input = input("Please enter a word or phrase: ")

# Empty string to receive the upper and lowercase letters from the user input
new_user = ''

# For loop that iterates through the user input, capitalising even indices of the string and putting odd indices in lower case. It then adds each letter to the empty string
for i in range(len(user_input)):
    if i % 2 == 0:
        new_user += user_input[i].upper()
    else:
        new_user += user_input[i].lower()

# Prints out the new string with the uppercase and lowercase letter transformation
print(new_user)

# Receives a user input sentence and assigns it to a variable
user_sentence = input("Please enter a sentence: ")

# Creates an empty list
new_sentence = []

# Splits the user input sentence by the spaces between the words
split_sentence = user_sentence.split(" ")

# For loop that alternately transforms each word in the split sentence list to upper and lowercase, appending each word to the empty list
for x in range(len(split_sentence)):
    if x % 2 == 1:
        new_sentence.append(split_sentence[x].upper())
    else:
        new_sentence.append(split_sentence[x].lower())

# Joins and prints the now filled new list back into a sentence, separating words by spaces
new_sentence = " ".join(new_sentence)
print(new_sentence)

