num1 = 0
operation = ""
flag = 0
while(True):
    if(flag == 0):
        num1 = int(input("What's the first Number : "))
    print("+\n-\n*\n/")
    operation = input("Pick an operation : ")
    ans = 0
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Invalid Operation")
        break
    num2 = int(input("Enter Second Number : "))
    if(operation == "+"):
        ans = num1 + num2
        print(ans)
    elif(operation == "-"):
        ans = num1 - num2
        print(ans)
    elif(operation == "*"):
        ans = num1 * num2
        print(ans)
    elif(operation == "/"):
        ans = num1 / num2
        print(ans)
    isOver = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation : ")
    if(isOver == 'y'):
        num1 = ans
        flag = 1
    else:
        flag = 0
        continue
print(ans)