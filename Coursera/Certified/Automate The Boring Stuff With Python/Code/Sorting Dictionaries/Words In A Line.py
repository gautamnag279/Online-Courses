stuff = dict()
line = input('Confess:')
words = line.split()
for word in words:
    stuff[word] = stuff.get(word , 0) + 1
print(stuff)
