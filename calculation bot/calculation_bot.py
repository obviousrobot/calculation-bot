print("Hello I am calculation bot.I will assist you today with your calculations")
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
operation=input("Please choose any one of these arthematic operations '+,-,*,/,%':")
if operation=="+":
    print("addition of the two numbers is:",num1+num2)
elif operation=="-":
    print("subtraction of the two numbers is:",num1-num2)
elif operation=="*":
    print("multiplication of the two numbers is:",num1*num2)
elif operation=="/":
    print("quotient of the two numbers is:",num1/num2)
elif operation=="%":
    print("remainder of the two numbers is:",num1%num2)
else:
    print("please enter an operator from the given list!")



