word = input("Wpisz słowo: ")
reversed =''.join(reversed(word))
print(reversed)

if reversed == word:
    print(True)
else:
    print(False)
