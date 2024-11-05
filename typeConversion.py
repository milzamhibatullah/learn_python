# year = input('year of birth? ')
# age = 2024-year
# print(age)
# code above with get an error
# reason: all value of inputs is String

# year = input('year of birth: ')
# # convert input to int
# # we make variable year to convert input string to int
# year = int(year)
# age = 2024-year
# print(age)

# lets check the type of input
# year = input('year of birth: ')
# print(type(year)) #in the terminal result is : <class 'str'>
# # convert input to int
# # we make variable year to convert input string to int
# year = int(year)
# print(type(year))#in the terminal result is : <class 'int'>
# age = 2024-year
# print(type(age))#in the terminal result is : <class 'int'>
# print(age)

#lets start to print the value of age combined with string
#expected is : your age is 29
year = input('year of birth: ')
print(type(year)) #in the terminal result is : <class 'str'>
# convert input to int
# we make variable year to convert input string to int
year = int(year)
print(type(year))#in the terminal result is : <class 'int'>
age = 2024-year
print(type(age))#in the terminal result is : <class 'int'>
#we should convert the int to string
#becaus function print cant concate the string with int directly
#use funtion str to convert
print('your age is '+str(age))

