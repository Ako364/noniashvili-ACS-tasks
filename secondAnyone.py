# Inputs time in the form h:m:s, splits separated by colon 
inputTime = input("Enter time in the form h:m:s to be convereted to seconds: ").split(":")

# Prints sum of hours*3600, m*60 (conversion to s), plus s
print((int(inputTime[0]) * 3600) + (int(inputTime[1]) * 60) + int(inputTime[2]))