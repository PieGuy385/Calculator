Cont = True
yn = ""

while Cont == True:
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator +, -, *, /, or ^: ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("You can't divide by zero")
        else:
            print(num1 / num2)
    elif op == "^":
        print(num1 ** num2)
    else:
        print("Invalid Operator")

    while Cont == True:
        yn = input("Would you like to continue? (y/n): ")
        if yn.lower() == "y":
            Cont = True
            break
        elif yn.lower() == "n":
            Cont = False
            break
        else:
            print("Please enter \"y\" or \"n\"")

print("Thanks for using my calculator :)")