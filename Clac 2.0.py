#First number input
num1=int(input("Enter the first number: "))

#Operator input
op=input("Choose the operator: ")

#Second number input
num2=int(input(Enter the second number: ))

#Addition operator
if op == '+':
   print(num1+num2)
#Subtraction operator
elif op == '-':
     print(num1-num2)
#Multiplication operator
elif op == '*':
     print(num1*num2)
#Division operator 
elif op == '/':
     print(num1/num2)
#Floor Division operator 
elif op == '//'
     print(num1//num2)
#Floor Multiplication
elif op == '**':
     print(num1**num2)
#If the user get another input accept from the above lines of code 
else:
    print('Get a valid input')
