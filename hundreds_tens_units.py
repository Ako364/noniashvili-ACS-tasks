a = int(input("please input an integer between 100 and 999: "))

while a < 100 or a > 999:
    print("input your number again")
    a = int(input("please input an integer between 100 and 999: "))

    if a >=100 and a <=999:
        hundreds = a // 100
        tens = (a - hundreds*100) // 10
        units = (a - hundreds*100 - tens*10)
        print(hundreds, "hundreds,", tens, "tens,", units, "units")
