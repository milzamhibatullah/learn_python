#this file we learn about variables
# variable it self means the place to store the value
# variable also can be mutable

#we make variable with name price and value is 100
#this type of variable is int
price = 100
#start to print variables
print(price) #the result is 100

#type of variable is float
discount = 0.5
print(discount)

#type of variable string
#clue is use double quotation
name="jams"
print(name)

#type of boolean
# we should use Capital at first character
# python is case sensitive
# fyi: if variable name is more than 1 word it should separated by underscore(_) or camelcase
is_discount = True
print(is_discount)

#python is dynamic ex: we can define the same variable but different value
#ex : price with value string
#python is interpreter to machine. so the structure of execute code it start from top to below
price=100
print(price)

#let start to try create variable with expression
price = price * discount
#the result is 50
#reason executed price is last variable in file (line 30) and opreate to times with discount variable
print(price)

# next we learn about converting ex: from float to in