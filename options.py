#get user input
num = int(input("input a number from 1 to 3: "))

#check option value
while num < 1 or num > 3:
    print("input your number again")
    num = int(input("input a number from 1 to 3: "))

    if num >=1 and num <=3:
        print("you have selected the option number: ", num)

    #end if
#end while