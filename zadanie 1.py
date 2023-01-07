# Napisz program, który sprawdzi czy podany wyraz jest palindromem.
# Czyli czy jest taki sam czytając od prawej co od lewej, np. kajak, anna

# 2.  Funkcja if, coś żeby przerzucać
# np. xanax
# 1 litera = ostatnia litera
# 2 litera = przedostatnia
# 3 liera jest stała,

word = 'XANAX'
for x in word:
    print(word[::-1])

for x in word:
    print(word)

if (word[::-1]) == (word):
    print(True)
else:
    print(False)






