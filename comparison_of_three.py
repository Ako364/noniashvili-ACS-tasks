# Inputs of numbers
firstNum = int(input("Enter your first number: "))
secondNum = int(input("Enter your second number: "))
thirdNum = int(input("Enter your third number: "))

#switches positions 
if firstNum > secondNum:
    firstNum,secondNum = secondNum,firstNum
# End if
if firstNum > thirdNum:
    firstNum,thirdNum = thirdNum,firstNum
# End if# End if
if secondNum > thirdNum:
    secondNum,thirdNum = thirdNum,secondNum
# End if

# Outputs in order
print (firstNum, " ", secondNum, " ", thirdNum)