# Input user's number
n = int(input("Enter your number: "))

factors = []

for i in range(1,n + 1):
    if n%i == 0:
        factors.append(i)
    # End if
# End for

print("Factors of ", n, " are ", factors)