#split entered sentence into words 
sentence = input("input a sentence:  ").split(" ")

i = 0
#print the words
while i < len(sentence):
    print(sentence[i])
    i = i + 1
