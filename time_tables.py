#input the value
num = int(input("type in a number between 1 and 10: "))

#validate the input
if num >= 1 and num <=10:
    n = 1 
    while n <= 10:
        print(num*n)
        n = n+1
else: 
    print("enter the valid number")
