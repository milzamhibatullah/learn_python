#we learn about method string default from python
# a lot of method can use, you can find on the documentation
# at this we learn some methond

#lets define variable with value of strings
message = "hi, i want to learn python like expert"
#lets get how much character
# we expect the result is 37
# the len is function
length = len(message)
print(length)

#lets capitalize all strings using method
print(message.upper())
#lets lower all strings using method
print(message.lower())
#lets capitalize of First Character at word
print(message.title())
#lets replace some words
#at this time i want to replace python to AI
print(message.replace('python','AI'))

#lest find some words is exist or not by variable
words = 'expert'
#lets print if words expert is exist on message variable
print(words in message) # the result is true