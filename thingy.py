f = open(input(), 'r')
lines = f.read().split('\n')
words = list()
# print(lines)

for line in lines:
    for word in line.split(' '):
        if not word in words and len(word) > 0:
            words.append(word)


words.sort()
print(words)
