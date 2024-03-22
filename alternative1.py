user_sentence = input("Please enter a sentence: ")

new_sentence = []

split_sentence = user_sentence.split(" ")


for x in range(len(split_sentence)):
    if x % 2 == 1:
        new_sentence.append(split_sentence[x].upper())
    else:
        new_sentence.append(split_sentence[x].lower())

new_sentence = " ".join(new_sentence)
print(new_sentence)

