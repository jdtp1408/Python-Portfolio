def add_prefix_un(word):
    # Adds the prefix 'un' to the beginning of a user-provided word
    un_word = "un"+word

    return un_word

# Prints the function in use with an example word
print(add_prefix_un("happy"))



def make_word_groups(vocab_words):
    # Extract prefix and words from the input list
    prefix = vocab_words[0]
    words = vocab_words[1:]
    
    # Apply the prefix to each word and join them with '::'
    prefixed_words = [f"{prefix}{word}" for word in words]
    result_str = " :: ".join([prefix] + prefixed_words)
    
    return result_str

# Prints the function in use with an example list
print(make_word_groups(['en', 'close', 'joy', 'lighten']))


def remove_suffix_ness(word):
    # If statement checks if the word before the suffix 'ness' has an i, in which case it adds a y
    if word[-5] == "i":
        result_str = word[:-5] + "y"
    else:
        result_str = word[:-4]
    
    return result_str

# Prints the function in use with an example word
print(remove_suffix_ness("weariness"))


def adjective_to_verb(sentence, index):
    # Removes the end punctuation of the user input sentence
    sentence = sentence[:-1]
    # Splits the sentence, selects the word at the user input index and adds the 'en' suffix
    en_word = sentence.split()[index] + "en"

    return en_word

# Prints the function in use with an example sentence
print(adjective_to_verb('It got dark as the sun set.', 2))
