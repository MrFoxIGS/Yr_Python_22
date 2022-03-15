import random

# nouns are naming words, make a list of at least 10 nouns
nounList = ["cat", "bird", "book", "pencil","dog"]

# adjectives are describing words, make a list of at least 10 adjectives
adjList = ["big", "small", "round", "flat", "red", "green"]

numb = str(random.randint(1, 100))

adj = random.choice(adjList)

noun = random.choice(nounList)

passWord = adj + noun + numb

print(passWord)
