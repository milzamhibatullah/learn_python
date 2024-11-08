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

numbers = [2,3,4,5,6,7]
total=0
sum1=sum(numbers)
print(sum1)
for number in  numbers:
    total+=number

print(total)

#get max number
max_number = max(numbers)
min_number = min(numbers)
print(max_number)
print(min_number)

max_bowl=0
#using for
for number in numbers:
    if number>max_bowl:
        max_bowl=number

print(max_bowl)