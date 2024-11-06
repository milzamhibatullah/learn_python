words = ['hello', 'jams','dev','here']
print(words)

print(words[0])
print(words[1:])
print(words[1:2])
print(words[-1])
words.reverse()
print(words)

for name in words:
    print('Name: '+name)

words.append(10)
print(words)
words.append('HIihi')
print(words)
words.remove(10)
print(words)

for name in words:
    if name.lower()=='hiihi' or name.lower()=='jams':
        words.remove(name)
        print(words)

words.insert(0,'jams')
print(words)

words.pop(-1)
print(words)

words.sort()
print(words)