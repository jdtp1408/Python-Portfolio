import spacy

nlp = spacy.load('en_core_web_md')


tokens = nlp('cat apple monkey banana tree')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Cat-monkey: 0.59
# Cat-banana: 0.22
# Monkey-banana: 0.40
# The model gives strong association to groupings such as animals and fruits, hence why cat-monkey is much higher than monkey-banana. 
# Nevertheless, it is clear that the model picked up on the association between monkeys and bananas (being that monkeys eat bananas)
# because the cat-banana similarity is far lower than the monkey-banana similarity.
        

# My example:
# Tree-cat 0.27
# Tree-apple 0.47
# Tree-monkey 0.35
# Tree-banana 0.43
# The example that I added was tree, which has some sort of association with all of the tokens. Tree-cat has the lowest, likely
# because the only real association between the tokens is the trope of cats getting stuck in trees, which is a reach.
# Tree-monkey has the second lowest similarity, which is slightly surprising because monkeys are known to swing on tree branches
# yet it is only slightly higher than 
#
