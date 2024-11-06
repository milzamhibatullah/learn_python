
operation= ""

while operation!="quit":
    operation= input("Enter your choice: ")
    if operation=="quit" or operation=="exit" or (operation!='+' and operation!='-' and operation!='*' and operation!='/'):
        break

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if operation=="+":
        print(a+b)
        break
    elif operation=="-":
        print(a-b)
        break
    elif operation=="*":
        print(a*b)
        break
    elif operation=="/":
        print(a/b)
        break


print("Thank you for playing")