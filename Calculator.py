#Calculator program in python

#User input for the first number
num1 = float(input("Enter the first number: "))
#User input for the operator
op=input("Choose operator: ")
#User input for the second number
num2 = float(input("Enter the second number:" ))

#Difine the operator (How t will it show the results)

if op == '+':
    print("You choosed for Addition ")
    print(num1+num2)
elif op == '-':
    print("You choosed for subtraction ")
    print(num1-num2)
elif op == '*':
    print("You choosed for multiplication ")
    print(num1*num2)
elif op == '/':
    print("Your choosed for division ")
    print(num1/num2)
else:
    print("Enter a valid operator")

    print("Some valid operators: "
          "+ "
          "- "
          "* "
          "/ ")
