import spacy
nlp = spacy.load('en_core_web_sm')

# Creates list of garden path sentences
gardenpathSentences = ["Fat people eat accumulates", "The man whistling tunes pianos", "Mary gave the child a Band-Aid", "That Jill is never here hurts", "The cotton clothing is made of grows in Mississipi"]

# For loop which first iterates through the gardenpathSentences list
# For each sentence in the list, the nested For loop tokenizes and then performs named entity recognition
for sentence in gardenpathSentences:
    for ent in nlp(sentence).ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

# Looks up meanings of descriptions provided by NER

# The entity was Mary, which is categorized under PERSON, representing people, including fictional people. The entity did make sense in terms of the word associated with it.
print(spacy.explain("PERSON"))


# The entity was Mississipi, which is categorized under GPE, representing countries, cities and states. The entity did make sense in terms of the word associated with it.
print(spacy.explain("GPE"))

# 


