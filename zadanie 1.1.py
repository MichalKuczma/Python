word = 'XANAX'

print("From left = ", word)

print("From right= ", word[::-1])

if word == word[::-1]:
    print(True)
else:
    print(False)