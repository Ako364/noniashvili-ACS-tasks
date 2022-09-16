#Asks user for inputs and inputs them
print("Enter your first number:")
firstNum = int(input())
print("Enter your second number:")
secondNum = int(input())

#If statement to compare size of firstNum and secondNum, prints the smallest first
if firstNum > secondNum:
    print(firstNum, " ", secondNum)
else:
    print(secondNum, " ", firstNum)
#end if