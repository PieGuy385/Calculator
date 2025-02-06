Continue = True

while Continue == True:
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
        print(num1 / num2)
    elif op == "^":
        print(num1 ** num2)
    else:
        print("Invalid Operator")

    yn = input("Would you like to continue? (y/n): ")
    if yn.lower() == "y":
        Continue = True
    elif yn.lower() == "n":
        Continue = False
    else:
        print("Please enter y or n")

print("Thanks for using my calculator :)")