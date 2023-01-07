word = 'DUPA'
for x in range(len(word)):
    print(word[x])
    print(len(word))
    if word[x] == word[-x-1]:
        print(True)
    else:
        print("Sorry, nie jest")
        break

