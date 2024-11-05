# string is series of character
# we can use single quotes or double qoutes
# name = "Jams"
# name2 = 'jams'
# print(name)
# print(name2)
#
# # we need to add qoutes inside string
# # we cant use same qoutes inside string
# #name = 'jams'dev''
# # print(name) #the result will give an error
# #lets try to different quotes
# name = 'jams "dev"'
# print(name)
#the result is jams "dev"

#lets start to get first character of name
#index start from 0
# print(name[0]) #the result is j
# #lest to get last of character in variable name
# #so if we need to get last character
# # we just reversed of index
# print(name[-1])
#
# #lets pick some character based on index
# # : means range
# print(name[0:4])
# #this code below to pick charater from index 4 to end of strings
# print(name[4:])

#lets jump to formatted string
#i want to make variable name with value string
# i want to make variable age with value of int
# we cant combine this variable using concatination
# we dont want to convert age usign str function
# we can us f as formatted
name = 'jams your age is '
age = 29
message = f"{name} {age}"
print(message)