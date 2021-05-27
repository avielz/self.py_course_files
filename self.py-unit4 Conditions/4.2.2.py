word = input("Enter a word: ")

#word = "Aviel"

#>>> Enter a word: sun
#NOT
#>>> Enter a word: bob
#OK
#>>> Enter a word: Borrow or rob
#OK

word = word.lower()
word = word.replace(" ", "")
print(word[-1::-1])

if word == word[-1::-1]:
    print("OK")
else:
	print("NOT")